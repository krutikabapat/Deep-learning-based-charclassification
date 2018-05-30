# Project Work

**TASK 1**

Generate 32 cross 32 pixel Images, 1000 each for 10 characters (0,1,2, ... ,9) and for 26 Alphabets (A,B, ... ,Z) using ImageMagick's "convert" function by writing code in Python Script (not using command line directly).

1. Images in this synthetic dataset should have random backgrounds. The backgrounds for each character should be selected randomly from the 100 background images downloaded in the previous steps. 

2. Characters in this synthetic dataset should be rendered using different randomly selected fonts. You can download fonts from Google Fonts. Use 25 of these fonts. 

3. The characters should be rendered with an arbitrary warp. (*here used position of the digit/character*)

4. Add a random amount of blur and noise to the training images. The amount of blur should not be very high to make the character unreadable. 

5. Using the 36000 images generated,use 80% for training purpose and 20% for test data for Image Clasification.

6. Now, using a suitable CNN type, we have to train the data. 

**Output of Task 1**

1. Trained and tested the model with Accuracy of **97.3 percent and loss of 0.03 percent.**

**References**

1.https://www.learnopencv.com/image-classification-using-convolutional-neural-networks-in-keras/
2.https://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/
3.http://cs231n.github.io/convolutional-networks/

**Errors, Issues**
1.For softmax to work properly,use tensorflow version 1.4.0 and above(1.7 is preferred, for othere below this, following error comes
  **TypeError: softmax() got an unexpected keyword argument 'axis'.**
  
2. For using GPU, CUDA 9.0 supports tensorflow 1.4 

3. In case the classification is for more than two classes, use learning rate of the order of 10^-3 to 10^-5.

