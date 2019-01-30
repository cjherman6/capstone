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

### Convolutional Filter:

A convolution consists of a little 3x3 matrix  (i.e. image kernel or filter) that multiplies every element of a photo matrix, and adds all the results of that multiplication:

![kernel](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/kernel.png)

When you input a photo, this can be converted into a matrix of pixels that represent the color or brightness in that pixel (grayscale, rgb, etc.):

![pixelated](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/photo_pixels.png)

Once this photo has been pixelated, you can pass the image kernel through each pixel of your image looking for activations.
* Any time it passes over a feature it’s built to look for (e.g. top edge) you get a positive (figure a); this is called an activation.  
* When it passes over a feature it’s not designed to detect, such as the opposite (e.g. bottom edge), you get a negative (figure b); or no activation at all, you get a low value (figure c)

##### Figure A
_Since it's light (high value pixels) in the upper row of this kernel, and dark (low value pixels) in the lower row of this kernel, the upper row is not cancelled out and creates a high value (i.e. activation) of 845_
![activation](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/activation.png)

##### Figure B
_Given the oppostite logic of the above photo we get a negative number_
![negative](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/activation_negative.png)

##### Figure C
_Since the it is light in the upper row, and light in the lower row, they cancel each other out and there is no activation_
![non-activation](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/not_activation.png)

A great example of how this works can be found here:
[http://setosa.io/ev/image-kernels/](http://setosa.io/ev/image-kernels/)

### Layers:

A CNN consists of various layers (input layer, hidden layers, fully connected layer, output layer)

A fantastic illustration of these various layers can be found on this video:
[Convolutional Neural Network Visualization by Otavio Good](https://www.youtube.com/watch?v=f0t-OCG79-U)

#### Input Layer
This is the first layer, in the below example it's a letter, in our example it's a dog

#### Hidden Layers

The first layer in this example is a *convolutional layer*, going through the same behavior as the image kernel above.  Activations occur anytime a horizontal edge is passed over:

![conv-layer](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/layer1.png)

After all the activations have been recorded, a non-linear operation called *RELU* (_Rectified Linear Unit_) occurs where you're essentially tossing out any negative values (e.g. the red pixels in the previous photo)

![conv-layer](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/layer2.png)

After RELU, this example goes through a *max pooling layer*, where it replaces every 2x2 section of your previous layer its maximum (_keeps it the same, but quarters the size of the matrix_)

![conv-layer](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/layer3.png)

In this example, the CNN combines the results of the previous convolutional layers (_This is where it becomes less intuitive what’s happening_)

![conv-layer](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/layer4.png)


++++
![conv-layer](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/layer5.png)
![conv-layer](https://s3.amazonaws.com/capstone-bucket-galvd83/readme/layer6.png)

A good example can be found here:
[Convolutional Layer](http://cs231n.github.io/convolutional-networks/#conv)

#### Fully Connected Layer
Fully-connected layers can be found within the hidden layers, but the last fully-connected layer is called the “output layer”

====================================================================================

## Content Based Recommender

### The Data

### How a Content Based Recommender Works
