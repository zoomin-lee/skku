# SKKU

##  Data_Structure 자료구조개론
- c언어와 python으로 자료구조개론 구현

##  Machine_Learning 기계학습
- ML_Assignment1
- ML_Assignment2
- ML_Assignment3
- ML_Assignment4
- ML_Assignment5
- ML_Assignment6
- Project1
- Porject2

##  cs231n 
- assignment1
- assignment2
- assignment3

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
Part 1. 

### A4

##  Introduction_to_deep_nerual_networks 심층신경망개론
- DNN_HW1
- DNN_HW2
- DNN_HW3
- DNN_HW4
- Final_Project

##  python_class
- 기본 python 문법을 복습하면서 공부한 내용

##  system_programming 시스템 프로그래밍
- 원리와 실제 리눅스 프로그래밍(창병모)

