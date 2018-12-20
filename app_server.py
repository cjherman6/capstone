import os
from flask import Flask, render_template, request, send_from_directory
import predict_function as pf

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
    predictions = []
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir('./images')
    print(image_names)
    for image_name in image_names:
        destination = '/'.join([target,image_name])
        predictions.append((image_name,pf.pred_output(destination)))
    print(predictions)
    return render_template('gallery.html', image_names=image_names,predictions=predictions)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
