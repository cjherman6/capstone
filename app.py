import os
import shutil
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, send_from_directory
import predict_function as pf
import recommender_function as rf
import pickle

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

pickle_in = open('app_data/translation_dict.pickle','rb')
translation_dict = pickle.load(pickle_in)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload',methods = ['POST'])
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

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('images',filename)

@app.route('/predictions')
def get_gallery():
    predictions, likelies, image_names = pf.pred_output()
    return render_template('predictions.html', image_names=image_names, image_predictions=zip(image_names,predictions,likelies))

@app.route('/survey')
def recommendation():
    predictions, _, _ = pf.pred_output()
    return render_template('survey.html',predictions=predictions)

@app.route('/recommendations',methods=['POST','GET'])
def display():
    # Average values across all traits as a starting point
    profile = rf.initial_profile()

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
    profile[np.array([2,12,13,19,21])] = exercise_needs
    profile[np.array([0,5,16])] = apartment_ready
    profile[6]= affection
    profile[np.array([7,9])] = fur_drool
    profile[10]= grooming
    profile[np.array([4,11])] = trainability
    profile[np.array([8,14])] = friendliness
    profile[np.array([17,1])] = kids
    profile[18] = intelligence
    profile[24] = sensitivity
    profile[25] = size
    profile[27] = tolerates_alone

    profile = np.array([profile])

    print("Profile Created: {}".format(profile))

    # Retrieving predictions from images folder
    predictions = {}
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir('./images')
    for image_name in image_names:
        destination = '/'.join([target,image_name])
        predictions[translation_dict[pf.pred_ind(destination)]] = image_name
    breeds = list(predictions.keys())

    # Combining profile from radio buttons and predictions from images folder
    # to output recommendations
    recommendations = rf.profile_recommender(profile,breeds)
    image_loc= [predictions[recommendation] for recommendation in recommendations]
    recommendations = [' '.join(recommendation.split('-')) for recommendation in recommendations]
    return render_template('recommendations.html',profile=profile,recommendations=recommendations,
    image_recommendations=zip(recommendations,image_loc))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
