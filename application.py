import os
import shutil
import numpy as np
import prediction_functions as pf
import recommender_function as rf
from flask import Flask, render_template, request, send_from_directory

application = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@application.route('/')
def index():
    return render_template('upload.html')

@application.route('/upload',methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if os.path.exists(target):
        shutil.rmtree(target)
    os.makedirs(target)

    for upload in request.files.getlist('file'):
        filename = upload.filename
        destination = '/'.join([target,filename])
        upload.save(destination)
    return render_template('complete.html',image_name=filename)

@application.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('images',filename)

@application.route('/predictions')
def get_gallery():
    predictions, likelies, image_names = pf.pred_output()
    return render_template('predictions.html', image_names=image_names, image_predictions=zip(image_names,predictions,likelies))

@application.route('/survey')
def recommendation():
    predictions, _, _ = pf.pred_output()
    return render_template('survey.html',predictions=predictions)

@application.route('/recommendations',methods=['POST','GET'])
def display():
    # Average values across all traits as an initial profile
    profile = rf.initial_profile()

    # Assigning radio button values to an array
    profile[np.array([2,12,13,19,21])] = request.form['exercise_needs']
    profile[np.array([0,5,16])] = request.form['apartment_ready']
    profile[6]= request.form['affection']
    profile[np.array([7,9])] = request.form['fur_drool']
    profile[10]= request.form['grooming']
    profile[np.array([4,11])] = request.form['trainability']
    profile[np.array([8,14])] = request.form['friendliness']
    profile[np.array([17,1])] = request.form['kids']
    profile[18] = request.form['intelligence']
    profile[24] = request.form['sensitivity']
    profile[25] = request.form['size']
    profile[27] = request.form['tolerates_alone']

    profile = np.array([profile])

    print("Profile Created: {}".format(profile))

    # Retrieving predictions from images folder
    predictions,breeds = pf.image_predictions()

    # Combining profile from radio buttons and predictions from images folder
    # to output recommendations
    rank, recommendations, image_loc = rf.rec_page_output(profile,breeds,predictions)

    return render_template('recommendations.html',recommendations=recommendations,
    image_recommendations=zip(rank, recommendations, image_loc))

if __name__ == "__main__":
    application.run(host='0.0.0.0')
