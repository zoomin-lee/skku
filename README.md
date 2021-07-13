# SKKU

##  Data_Structure 자료구조개론
- c언어와 python으로 자료구조개론 구현

##  Machine_Learning 기계학습
### ML_Assignment1
Navie Bayes 구현하기

### ML_Assignment2
Linear SVM 구현하기

### ML_Assignment3
Decision Tree 구현하기

### ML_Assignment4
Logistic Regression 구현하기

### ML_Assignment5
Multi-layer Perceptron 구현하기

### ML_Assignment6
Linear Regression 구현하기

### Project
to design & implement an ML-based applicationto predict whether the person who appears in the given video has depression or not.
- OpenSmilefeatures : 384 features
- FaceEmotionFeatures : Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise

#### Project1
- Do not use machine learning classifiers already developed in other libraries(e.g.,scikit-learn)

#### Project2
- Use machine learning classifiers already developed in other libraries(e.g.,scikit-learn)

##  cs231n 
### assignment1
In this assignment you will practice putting together a simple image classification pipeline based on the k-Nearest Neighbor or the SVM/Softmax classifier. The goals of this assignment are as follows:

- Understand the basic Image Classification pipeline and the data-driven approach (train/predict stages)
- Understand the train/val/test splits and the use of validation data for hyperparameter tuning.
- Develop proficiency in writing efficient vectorized code with numpy
- Implement and apply a k-Nearest Neighbor (kNN) classifier
- Implement and apply a Multiclass Support Vector Machine (SVM) classifier
- Implement and apply a Softmax classifier
- Implement and apply a Two layer neural network classifier
- Understand the differences and tradeoffs between these classifiers
- Get a basic understanding of performance improvements from using higher-level representations as opposed to raw pixels, e.g. color histograms, Histogram of Gradient (HOG) features, etc.

### assignment2
In this assignment you will practice writing backpropagation code, and training Neural Networks and Convolutional Neural Networks. The goals of this assignment are as follows:

- Understand Neural Networks and how they are arranged in layered architectures.
- Understand and be able to implement (vectorized) backpropagation.
- Implement various update rules used to optimize Neural Networks.
- Implement Batch Normalization and Layer Normalization for training deep networks.
- Implement Dropout to regularize networks.
- Understand the architecture of Convolutional Neural Networks and get practice with training them.
- Gain experience with a major deep learning framework, such as TensorFlow or PyTorch.

### assignment3
In this assignment, you will implement recurrent neural networks and apply them to image captioning on the Microsoft COCO data. You will also explore methods for visualizing the features of a pretrained model on ImageNet, and use this model to implement Style Transfer. Finally, you will train a Generative Adversarial Network to generate images that look like a training dataset! The goals of this assignment are as follows:

- Understand the architecture of recurrent neural networks (RNNs) and how they operate on sequences by sharing weights over time.
- Understand and implement both Vanilla RNNs and Long-Short Term Memory (LSTM) networks.
- Understand how to combine convolutional neural nets and recurrent nets to implement an image captioning system.
- Explore various applications of image gradients, including saliency maps, fooling images, class visualizations.
- Understand and implement techniques for image style transfer.
- Understand how to train and implement a Generative Adversarial Network (GAN) to produce images that resemble samples from a dataset.

##  Introduction_of_computer_vision 컴퓨터비전개론
### A1
Part 1. Image Filtering : A1_image_filtering.py
1-1 Image filtering by Cross-Correlation
- function filtered_img = cross_correlation_1d( img , kernel ) : should distinguish between between vertical and horizontal kernels
- function filtered_img = cross_correlation_2d( img , kernel )
- the sizes of img and filtered_img should be identical. 
- Cannot use any built-in function that performs cross-correlation, colvolution, filtering or image padding. 

1-2 The Gaussian Filter
- function kernel = get_gaussian_filter_1d ( size , sigma )
- function kernel = get_gaussian_filter_2d ( size , sigma )
- Perform the Gaussian filtering by applying vertical and horizontal 1D kernels sequantially, and compare the result with a filtering with a 2D kernel
- Cannot use any built-in function that produces Gaussian filters. 

![image](https://user-images.githubusercontent.com/65997635/125275262-c5779b80-e349-11eb-9743-8767d2af1a39.png)

Part 2. Edge Detection : A1_edge_detection.py
2-1 Implement a function that returns the image gradient
- function mag, dir = compute_image_gradient ( img )

![image](https://user-images.githubusercontent.com/65997635/125275284-cd374000-e349-11eb-9bc1-80347ba505ed.png)
![image](https://user-images.githubusercontent.com/65997635/125275299-d32d2100-e349-11eb-81d6-bed06f4d81dd.png)

2-2 Implement a function that performs Non-maximum Suppression (NMS)
- function suppressed_mag = non_maximum_suppression_dir ( mag , dir )
- implement an approximated version of NMS by quantizing the gradient directions into 8 bins. If a direction is represented by an angle in degrees, we can map the direction to the closet representative angle among [0°, 45°, … ,315°]

![image](https://user-images.githubusercontent.com/65997635/125275321-d88a6b80-e349-11eb-8704-2cba253844af.png)

![image](https://user-images.githubusercontent.com/65997635/125275337-db855c00-e349-11eb-8e5a-48c7c96f4986.png)
![image](https://user-images.githubusercontent.com/65997635/125275351-df18e300-e349-11eb-8106-ef65539c24de.png)

Part 3. Corner Detection : A1_corner_detection.py
3-1 Implement a function that returns corner response values
- function R = compute_corner_response ( img )

3-2 Thresholding and Non-maximum Suppression (NMS): 
- Change the color of pixels having corner response greater than a threshold of 0.1 to green.

![image](https://user-images.githubusercontent.com/65997635/125275366-e2ac6a00-e349-11eb-97b5-92994cff4a38.png)
![image](https://user-images.githubusercontent.com/65997635/125275375-e63ff100-e349-11eb-9d98-69acef063eb4.png)
- Implement a function that compute local maximas by non-maximum suppression
- function suppressed_R = non_maximum_suppression_win ( R , winSize )

![image](https://user-images.githubusercontent.com/65997635/125275394-e9d37800-e349-11eb-83a9-864e6e75ad84.png)
![image](https://user-images.githubusercontent.com/65997635/125275405-ed66ff00-e349-11eb-8a7f-586e39b784cb.png)

### A2
Part 1. 2D Transformations : A2_2d_transformation.py
- Implement a function that returns a plane where the transformed image is displayed. The function gets two parameters, an image img and a 3 × 3 affine transformation matrix M. The vertical and horizontal sizes of the plane is fixed to 801 × 801 and the origin (0, 0) is corresponding to the pixel at (400, 400). You also need to draw two arrows to visualize 𝑥 and 𝑦 axes.
- function plane = get_transformed_image ( img , M )
- Extra credit: We have some artifacts when we enlarge or rotate the image as shown in the above examples. Reducing the artifacts gets extra credits.

![image](https://user-images.githubusercontent.com/65997635/125275431-f8219400-e349-11eb-8748-d6f1dede97b2.png)
![image](https://user-images.githubusercontent.com/65997635/125275448-fbb51b00-e349-11eb-97ac-ee5a6e82a1e3.png)

Part 2. Homography : A2_homography.py
2-1 Feature detection, description and matching
- orb = cv2.ORB_create()
- kp = orb.detect( img , None )
- kp, des = orb.compute( img , kp )
- Perform feature matching between two images (‘cv_desk.png’ and ‘cv_cover.jpg’), and display top-10 matched pairs according to feature similarities
- cannot use any built-in function that directly performs feature matching

![image](https://user-images.githubusercontent.com/65997635/125275462-ff48a200-e349-11eb-8390-4adab3cdf28c.png)

2-2 Computing homography with normalization
- Implement a function that returns a homography from a source image to a destimation image. The function gets two 𝑁 × 2 matrices, srcP and destP, where 𝑁 is the number of matched feature points and each row is a location in the image, and returns a 3 × 3 transformation matrix. Note that, the number of matches 𝑁 should be equal or greater than 15, 𝑁 ≥ 15.
- function H = compute_homography ( srcP , destP )

2-3 Computing homography with RANSAC	
- function H = compute_homography_ransac ( srcP , destP , th )
- The parameter th is used to determine whether a point is inlier or outlier.
- your function should produce the homography within 3 seconds.

2-4 Image wraping
- Wraps ‘cv_cover.jpg’ to the dimensions of ‘cv_desk.png’. Display the warpped image of ‘cv_cover.jpg’ and the composed image. You can use cv2.warpPerspective(...) for the wrapping. 
- Compare the results of the homography with normalization and RANSAC

![image](https://user-images.githubusercontent.com/65997635/125275478-07084680-e34a-11eb-84e7-02590533c6f3.png)
![image](https://user-images.githubusercontent.com/65997635/125275487-0b346400-e34a-11eb-8649-27141eed9a80.png)

![image](https://user-images.githubusercontent.com/65997635/125275495-0ec7eb00-e34a-11eb-9276-29a0fce4a5db.png)
![image](https://user-images.githubusercontent.com/65997635/125275507-15566280-e34a-11eb-9737-6bf3ee6ca028.png)

2-5 Image Stiching
- Read ‘diamondhead-10.png’ and ‘diamondhead-11.png’, and stitch them based on the homography computed with RANSAC. Display the result.

![image](https://user-images.githubusercontent.com/65997635/125275524-1ab3ad00-e34a-11eb-9090-e5c6e22bf2a4.png)

- In order to reduce the artifacts on the boundary of two images, perform a simple gradation based blending:

![image](https://user-images.githubusercontent.com/65997635/125275531-1e473400-e34a-11eb-8adb-d0350d931aa1.png)

### A3
Part 1. Fundamental Matrix : A3_Fmat.py
- The feature correspondences between two images are also provided in ‘temple_matches.txt’ file.
- M = np.loadtxt( ‘temple_matches.txt’ )

- Implement the Eight-point algorithm to compute the fundanmental matrix
- function F = compute_F_raw ( M )

- Implement the Eight-point algorithm with a normalization
- function F = compute_F_norm ( M )

- Implement your own algorithm to compute the fundanmental matrix
- function F = compute_F_mine ( ... )
- It should return the result within 3 seconds.

Part 2. Visualization of epipolar lines
- Implement a script that performs the followings:
- Randomly select 3 correspondances: (𝑝1 ↔ 𝑞1), (𝑝2 ↔ 𝑞2), and (𝑝3 ↔ 𝑞3)
- Compute 6 epipolar lines 𝑙1, 𝑙2, 𝑙3, 𝑚1, 𝑚2, 𝑚3 corresponding to 𝑝1, 𝑝2, 𝑝3, 𝑞1, 𝑞2, 𝑞3.

![image](https://user-images.githubusercontent.com/65997635/125275544-21dabb00-e34a-11eb-938c-a673ea84bf75.png)


##  Introduction_to_deep_nerual_networks 심층신경망개론
### DNN_HW1
Linear Regression
- Implement training and evaluation function in ‘models/LinearRegression.py’ (‘train’ and ‘forward’ respectively) using the gradient descent method. Training should be based on minibatch. 
- Implement the linear regression with scikit-learn library in ‘/linear_sklearn.py’. The linear regression using scikit-learn library uses an analytic solution.

Logistic Regression
- Implement training and evaluation function in ‘models/ LogisticRegression.py’ (‘train’ and ‘forward’ respectively) using the gradient descent method. 
- Implement the logistic regression with scikit-learn library in ‘/linear_sklearn.py’. 


### DNN_HW2
- Implement functions in ReLU, Sigmoid, Tanh, FCLayer, SoftmaxLayer, L2Regularization in ‘Answer.py’.
(a) [Activation Layer] Implement sigmoid, ReLU, tanh activation functions in ‘Answer.py’ (‘Sigmoid’,
‘ReLU’, ‘Tanh’).
(b) [Fully Connected Layer] Implement a fully-connected layer in ‘Answer.py’ (‘FCLayer’).
(c) [Softmax Layer] Implement the softmax layer in ‘Answer.py’ (‘SoftmaxLayer’).

- [DNN with different activation layer] Report test accuracy on MNIST using three different activation functions (sigmoid, ReLU, and tanh) with a given DNN architecture and parameters. Explain the differences among three activation functions based on the result (use only one activation function in one experiment among sigmoid, ReLU, and tanh).

- [Deep Neural Networks] optimize your model architecture (# of hidden layers, # of hidden nodes, # of epochs, learning rate etc.) to achieve the best results on FashionMNIST using ‘main.py’. Report your best test accuracy with your fine-tuned hyperparameters. Show the plot of training and validation accuracy every epoch on each case. 


### DNN_HW3
- Implement Multilayer Perceptron (MLP) models in ‘MLP_classifier.py’ and ‘MLP_regressor.py.’
(a) [Regression] Implement __init__, forward, and predict method functions in ‘MLP_regressor.py.’
(b) [Classification] Implement __init__, forward, and predict method functions in ‘MLP_classifier.py.’

- [Regression with different architectures] Adjust the model settings (number of hidden layers, number of hidden nodes, number of epochs, learning rate, etc.) to obtain the best results over the House dataset using ‘main_regressionpy.’

- [Classification with different architectures] Adjust the model settings (number of hidden layers, number ofhidden nodes, number of epochs, learning rate, etc.) to get the best results over FashionMNIST using ‘main_classification.py.’

### DNN_HW4
- Implement CNN models in ‘AlexNet.py’ and ‘ResNet.py.’
(a) [AlexNet] Implement AlexNet in ‘models/AlexNet.py’.
(b) [ResNet] Implement ResNet-18 in ‘model/ResNet.py’.

- [Random Search with MNIST] Adjust the model settings (# of hidden layers, # of hidden nodes, # of epochs, learning rate, etc.) with random search to get the best results over MNIST dataset using ‘main_random_search.py’

- [CNN with Fashion MNIST] Choose a model and adjust the model settings (# of hidden layers, # of hidden nodes, # of epochs, learning rate, etc.) to get the best results over FashionMNIST dataset using ‘main_classification.py.’

### Final_Project
Semi-supervised learning for image classification: The goal of our final project is to build a machine learning model for image classification, where a few data are only labeled and most of the data are unlabeled. Therefore, it is essential to utilize a large amount of unlabeled data to improve the accuracy of your model.

Dataset: 
- Train(labeled)/Train(unlabeled)/Test data: 5,000 / 35,551 / 10,000
- Input: 32x32 image with RGB channels.
- Classes: 10 (Detailed information on labels is not provided.)

##  python_class
- 기본 python 문법을 복습하면서 공부한 내용

##  system_programming 시스템 프로그래밍
- 원리와 실제 리눅스 프로그래밍(창병모)

