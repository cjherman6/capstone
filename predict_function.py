from fastai.imports import *
from fastai.torch_imports import *
from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *


torch.cuda.set_device(0)

PATH = "data/dogbreed/"
sz = 224
arch = resnext101_64
bs = 58
label_csv = f'{PATH}labels.csv'
n = len(list(open(label_csv))) - 1 # header is not counted (-1)
val_idxs = get_cv_idxs(n) # random 20% data for validation set
label_df = pd.read_csv(label_csv)

def get_data(sz, bs): # sz: image size, bs: batch size
    tfms = tfms_from_model(arch, sz, aug_tfms=transforms_side_on, max_zoom=1.1)
    data = ImageClassifierData.from_csv(PATH, 'train', f'{PATH}labels.csv', test_name='test',
                                       val_idxs=val_idxs, suffix='.jpg', tfms=tfms, bs=bs)

    return data if sz > 300 else data.resize(340, 'tmp') # Reading the jpgs and resizing is slow for big images, so resizing them all to 340 first saves time

data = get_data(sz, bs)

learn = ConvLearner.pretrained(arch, data, precompute=False)
learn.load('299_pre')

def prediction(fn):
    root = 'app_data/prediction_images/'
    img = plt.imread(root+fn)
    plt.imshow(img);

    trn_tfms, val_tfms = tfms_from_model(arch, sz)
    ds = FilesIndexArrayDataset([fn], np.array([0]), val_tfms,root)
    dl = DataLoader(ds)
    preds = learn.predict_dl(dl)
    prediction = learn.data.classes[np.argmax(preds)]
    likelies = [learn.data.classes[breed] for breed in np.argsort(preds)[0][-5:]][3::-1]
    print('Prediction: {}'.format(prediction.capitalize()))
    print('Other likely breeds: {0}, {1}, {2}, {3}'.format(*likelies))

def pred_output(fn):
    root = 'app_data/prediction_images/'
    trn_tfms, val_tfms = tfms_from_model(arch, sz)
    ds = FilesIndexArrayDataset([fn], np.array([0]), val_tfms,root)
    dl = DataLoader(ds)
    preds = learn.predict_dl(dl)
    prediction = learn.data.classes[np.argmax(preds)]
    return prediction    
    
if __name__ == '__main__':
    test_output = pred_output('aawl1.jpg')
    print(test_output)
