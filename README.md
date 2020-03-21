# Number-Plate-Detection

The main objective of this project is to design an efficient automatic authorized vehicle identification system using the vehicle number
plate. The system is implemented on the entrance for security control of a highly restricted area like Military Zones, or area around 
top Government offices, e.g., Parliament, Supreme Court The proposed system has three major stages:

The proposed system has three major stages:
1-License Plate Detection using OpenCV
2-Character Segmentation
3-Character Recognition using Convolutional Neural Network
(CNN)

License Plate Detection:
We have to resize the captured image in to Required Size and then grayscale it resizing help us to avoid any problems with bigger resolution
images, make sure the number plate still remains in the frame after resizing. Gray scaling is common in all image processing steps. This
speeds up other following process since we no longer have to deal with the many color details when processing an image. The image would be
transformed in two colours black and White. Every image will have useful and useless information, in this case for us only the license plate is the
useful information the rest are pretty much useless for our program. This useless information is called noise. Normally using bilateral filter it will
remove unwanted details from image. The next step is to perform edge detection and then start looking for contours on our image. Once the
counters have been detected we sort them from big to small and consider only the first 10 results ignoring the others. In our image the counter could
be anything that has a closed surface but of all the obtained results the license plate number will also be there since it is also a closed surface.
To filter the license plate image among the obtained results, we will loop though all the results and check which has a rectangle shape contour with
four sides and closed figure. Since a license plate would definitely be a rectangle four sided figure.

Character Segmentation & Feature Extraction:
Character segmentation is an operation that seeks to decompose an image
of a sequence of charac- ters into subimages of individual symbols. It is
one of the decision processes in a system for optical character recognition
(OCR).In feature extraction stage each character is represented as a feature
vector, which becomes its identity

Character Recognition Using CNN:
In order to predict the character present in Number plate we use Machine
learning Technique called CNN (Convolutional Neural Network). In deep
learning, a convolutional neural network is a class of deep neural
networks, most commonly applied to analyzing image
