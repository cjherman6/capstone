import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, send_from_directory
import recommender_function as rf
df = pd.read_csv('app_data/breed_traits.csv',index_col='Unnamed: 0')

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('radio.html')

@app.route('/display',methods=['POST'])
def display():
    profile = df.describe().T['mean'].values

    qs = ['exercise_needs', 'apartment_ready', 'affection', 'fur_drool', 'grooming', 'trainability', 'friendliness', 'kids', 'intelligence', 'sensitivity', 'size', 'tolerates_alone', 'temperature']

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



    # activity = request.form['activity_level']
    # grooming = request.form['grooming']

    # i = np.array([2,12,13,19,21])
    # if activity == 3:
    #     profile[i] = 5
    # elif activity == 2:
    #     profile[i] = 3
    # elif activity == 1:
    #     profile[i] = 1
    #
    # i = np.array([7,9])
    # if grooming == 3:
    #     profile[i] = 1
    # elif grooming == 2:
    #     profile[i] = 3
    # elif grooming == 1:
    #     profile[i] = 5

    profile = np.array([profile])
    print(profile)

    recommendations = rf.profile_recommender(profile)
    print(recommendations)
    return render_template('display.html',profile=profile,recommendations=recommendations)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
