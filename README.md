# PROJECT STATEMENT
### Helping you find the right dog

According to a recent survey by the APPA, roughly 23% of dog adoptions come from a shelter. This can make knowing the breed of your dog and the considerations of your specific breed difficult. This app is designed to get you started on knowing the possible breed of dogs you’re interested in as well as recommending the best fit based on your given photos and your preferences.

The initial motivation of this project was to experiment with image classification using a neural network as well as combining those results with a recommender system. The end product will hopefully guide you along your process of finding a new family member with an easy to use interface that allows you to upload photos of potential dogs you're interested in, tell us a little bit about yourself, and output recommendations.


To visit the website, click here:

http://3.89.14.141:5000/

![Home Page](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/home_page.png)

# METHODS USED
### Convolutional Neural Network & Content Based Recommender

## Convolutional Neural Network (CNN)

This app uses a CNN to let users upload various photos of dogs and get a prediction of what breed the dog could be.  The model is currently trained on 120 different dog breeds coming from the Kaggle Dog Breed Identification competition.  Adding 100+ more breeds is something I plan on expanding and building later on.

### How CNNs Work

#### Convolutional Filter:

A convolution consists of a little 3x3 matrix  (i.e. image kernel or filter) that multiplies every element of a photo matrix, and adds all the results of that multiplication:

![kernel](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/kernel.png)

When you input a photo, this can be converted into a matrix of pixels that represent the color or brightness in that pixel (grayscale, rgb, etc.):

![pixelated](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/photo_pixels.png)

Once this photo has been pixelated, you can pass the image kernel through each pixel of your image looking for activations.
* Any time it passes over a feature it’s built to look for (e.g. top edge) you get a positive (figure a); this is called an activation.  
* When it passes over a feature it’s not designed to detect, such as the opposite (e.g. bottom edge), you get a negative (figure b); or no activation at all, you get a low value (figure c)

##### Figure A
![activation](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/activation.png)
_

##### Figure B
![negative](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/activation_negative.png)

##### Figure C
![non-activation](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/not_activation.png)


A great example of how this works can be found here:
![http://setosa.io/ev/image-kernels/](http://setosa.io/ev/image-kernels/)

====================================================================================
====================================================================================
====================================================================================

## Content Based Recommender

### The Data

### How a Content Based Recommender Works
