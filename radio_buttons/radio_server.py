import os
import numpy as np
from flask import Flask, render_template, request, send_from_directory
import recommender_function as rf

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('radio.html')

@app.route('/display',methods=['POST'])
def display():
    # data = request.form['radio']
    # print(data)
    activity = request.form['activity_level']
    grooming = request.form['grooming']
    profile = np.zeros(31)
    if activity == 3:
        profile[:15] = 3
    elif activity == 2:
        profile[:15] = 2
    else:
        profile[:15] = 1

    if grooming == 3:
        profile[15:] = 6
    elif grooming == 2:
        profile[15:] = 5
    else:
        profile[15:] = 4
    profile = np.array([profile])
    print(profile)
    print('Activity gave back {}, grooming gave back: {}'.format(activity,grooming))

    recommendations = rf.profile_recommender(profile)
    print(recommendations)
    return render_template('display.html',activity=activity,grooming=grooming,profile=profile,recommendations=recommendations)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
