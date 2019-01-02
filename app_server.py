import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, send_from_directory
import predict_function as pf
import recommender_function as rf
import pickle

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv('app_data/breed_traits.csv',index_col='Unnamed: 0')
pickle_in = open('app_data/translation_dict.pickle','rb')
translation_dict = pickle.load(pickle_in)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload',methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # e.g. /Users/Chris/Desktop/app_restart/images/
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for upload in request.files.getlist('file'):
        # e.g. <FileStorage: 'dog2.jpeg' ('image/jpeg')>
        print(upload)
        filename = upload.filename
        # extension = os.path.splittext(filename)[1]
        destination = '/'.join([target,filename])
        # e.g. /Users/Chris/Desktop/app_restart/images//dog2.jpeg
        print(destination)
        upload.save(destination)
    # jinja command takes in image_name for: {{ url_for('static',filename=image_name)  }}"
    return render_template('complete.html',image_name=filename)

    # stores and downloads file
    # return send_from_directory('images',filename,as_attachment=True)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('images',filename)

@app.route('/gallery')
def get_gallery():
    print('testing')
    predictions = []
    likelies = []
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir('./images')
    print(image_names)
    for image_name in image_names:
        destination = '/'.join([target,image_name])
        predictions.append(' '.join(pf.pred_output(destination).split('_')).title())
        likelies.append(pf.pred_likelies(destination))
    print(predictions)
    print(likelies)

    return render_template('gallery.html', image_names=image_names, image_predictions=zip(image_names,predictions,likelies))

@app.route('/recommendation')
def recommendation():
    predictions = []
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir('./images')
    for image_name in image_names:
        destination = '/'.join([target,image_name])
        predictions.append(pf.pred_output(destination))
    print(predictions)
    breeds = [translation_dict[breed] for breed in predictions]
    print(breeds)

    return render_template('recommendation.html',predictions=predictions)

########################################################################
########################################################################
########################################################################
########################################################################

@app.route('/display',methods=['POST','GET'])
def display():
    # Average values across all traits as a starting point
    profile = df.describe().T['mean'].values

    # Getting values from all radio buttons
    exercise_needs = request.form['exercise_needs']
    apartment_ready = request.form['apartment_ready']
    affection = request.form['affection']
    fur_drool = request.form['fur_drool']
    grooming = request.form['grooming']
    trainability = request.form['trainability']
    friendliness = request.form['friendliness']
    kids = request.form['kids']
    intelligence = request.form['intelligence']
    sensitivity = request.form['sensitivity']
    size = request.form['size']
    tolerates_alone = request.form['tolerates_alone']

    # Assigning radio button values to an array
    exercise_needs_i = np.array([2,12,13,19,21])
    profile[exercise_needs_i] = exercise_needs
    apartment_ready_i = np.array([0,5,16])
    profile[apartment_ready_i] = apartment_ready
    profile[6]= affection
    fur_drool_i = np.array([7,9])
    profile[fur_drool_i] = fur_drool
    profile[10]= grooming
    profile[np.array([4,11])] = trainability
    profile[np.array([8,14])] = friendliness
    profile[np.array([17,1])] = kids
    profile[18] = intelligence
    profile[24] = sensitivity
    profile[25] = size
    profile[27] = tolerates_alone

    profile = np.array([profile])
    print(profile)

    # Retrieving predictions from images folder
    predictions = {}
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir('./images')
    for image_name in image_names:
        destination = '/'.join([target,image_name])
        predictions[translation_dict[pf.pred_output(destination)]] = destination
    print(predictions)
    breeds = list(predictions.keys())

    # Combining profile from radio buttons and predictions from images folder
    # to output recommendations
    recommendations = rf.profile_recommender(profile,breeds)
    print(recommendations)
    image_loc=predictions[recommendations]
    print(image_loc)
    return render_template('display.html',profile=profile,recommendations=recommendations,
    image_recommendations=zip(recommendation,image_loc))

    # return render_template('gallery.html', image_names=image_names, image_predictions=zip(image_names,predictions,likelies))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
