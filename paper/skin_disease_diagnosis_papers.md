Dermatologist vs Neural Network

15 Jun 2020

- HAM 10000 dataset which offers 10015 images belonging to 7 classes of ckin disease.
- 9013 images as the training set and 1002 images as the validation set.
- data augmentation increases the size of dataset hence it also helps in reducing overfitting.
- categorical cross-entropy loss function.
- Adam has β1 and β2 as hyper-parameters.
- For training our model we have set β1 = 0.9 and β2 = 0.999..
- start at a learning rate of 0.001 and it is decayed by a factor of 10 each time the validation loss plateaus after an epoch.
- pick the model with the lowest validation loss in this process.
- batch size used is 90 images.
- The precision, recall and f1 score of each class was impressive enough to outshine the models based on Transfer Learning.
- The Training accuracy achieved is 93% while the validation accuracy achieved is 89%.
- the model we built is far better or as good as ResNet50, InceptionV3, Vgg19, and MobileNetV2.

https://paperswithcode.com/paper/dermatologist-vs-neural-network



SkinGPT-4: An Interactive Dermatology Diagnostic System with Visual Large Language Model

8 Jun 2023

- SkinGPT-4 leverages a fine-tuned version of MiniGPT-4, trained on an extensive collection of skin disease images (comprising 52,929 publicly available and proprietary images) along with clinical concepts and doctors’ notes.
- In the initial step, SkinGPT-4 aligns visual and textual clinical concepts, enabling it to recognize medical features within skin disease images and express those medical features with natural language. In the subsequent step, SkinGPT 4 learns to accurately diagnoses the specific types of skin diseases. This comprehensive training methodology ensures the system’s proficiency in analyzing and classifying various skin conditions.
- Our datasets include two public datasets and our private in-house dataset, where the first public dataset was used for the step 1 training, and the second public dataset and our in-house dataset were used for the step 2 training.
- The first public dataset named SKINCON is the first medical dataset densely annotated by domain experts to provide annotations useful across multiple disease processes.
- The second public dataset named the Dermnet contains 18,856 images, which are further classified into 15 classes by our board-certified dermatologists.
- Our private in-house dataset contains 30,187 pairs of skin disease images and corresponding doctors’ descriptions.
- The training and inference procedures were conducted on a workstation equipped with 252 GB RAM, 112 CPU cores, and two NVIDIA V100 GPUs, which provided the computational resources necessary for efficient model training and inference.
- To assess the reliability and effectiveness of SkinGPT-4, we assembled a dataset comprising 150 real-life cases of various skin diseases as shown in Table 2. Interactive diagnosis sessions were conducted with SkinGPT-4, utilizing four specific prompts:
- 1. Could you describe the skin disease in this image for me?
- 2. Please provide a paragraph listing additional features you observed in the image.
- 3. Based on the previous information, please provide a detailed explanation of the cause of this skin disease.
- 4. What treatment and medication should be recommended for this case?
- The SKINCON dataset can be accessed at https://skincon-dataset.github.io/. The Dermnet dataset can be accessed at https: //www.kaggle.com/datasets/shubhamgoel27/dermnet.
- SkinGPT-4 is publicly available at https: //github.com/JoshuaChou2018/SkinGPT-4.

https://paperswithcode.com/paper/skingpt-a-dermatology-diagnostic-system-with



Skin lesion classification of dermoscopic images using machine learning and convolutional neural network

19 December 2022

- In the proposed work, Convolutional Neural Networks (CNN) and Machine Learning algorithms are used to accurately classify pigmented skin lesions in dermoscopic images to detect malignant skin lesions as early as feasible.
- The HAM10000 dataset which consists of 10015 images has been used in the proposed work.
- The HAM10000 dataset is a vast collection of dermoscopic images of pigmented skin lesions which are very common from multiple sources.
- Image pre-processing
- Step 1 - ordering the dataset
- As the dataset images are out of order, sorting each image within each folder by the seven diseases is the necessary.
- Step 2 - Image resizing
- All the images in the folder are resized to 220*220 before processing into different machine learning models.
- For the customized CNN model, images are scaled to 96 × 96 with a depth of 3 to speed up the process. Then we have converted the images into a NumPy array to get the value of each pixel of the image.
- Step 3 - Data augmentation
- To train the machine learning models, the proposed method used Horizontal Flip augmentation i.e., shifting all pixels of an image in a horizontal direction
- In the CNN model since we are working with a finite number of data points (each class has 200 images), we have applied random transformations (rotations, shearing, etc.) to train.
- Feature extraction
- The color of the skin lesion image is quantified using a Colour Histogram. The shape of the skin lesion is quantified using Hu Moments.
- The texture of the skin lesion is quantified using a Haralick Texture. These features are chosen because the color, shape, and texture are the only properties that dominate in the lesion zone.
- Data splitting
- The total number of images obtained from the HAM1000 dataset for Machine Learning model training is 700 (100 images from each class), 560 of which images represent 80% for training and 140 images represent 20% for testing.
- Image classification
- The proposed work used machine learning models and a Convolutional Neural Network model to train and test the image dataset and evaluated the performance using the various parameters, namely, Accuracy, Precision, Recall, and F1-score.
- Convolutional neural network
- To build a CNN, Tensorflow and Keras libraries were used to build and implement the model in Python 3.7.9.
- Model hyperparameters
- Adam is the most widely used optimization method for training deep neural networks today because it is simple to use, computationally efficient, and effective when dealing with enormous amounts of data and parameters.
- The Multi-Class calculates the loss value using the “categorical cross-entropy” loss function.
- Found that 150 epochs result in a model with low loss and no overfitting to the training set through experimentation (or not overfitted as best as we can).
- Several early tests with batch sizes of 5, 10, 20, and 40 found that batch size 32 produced the best results.
- The rate of learning is initially set to 0.001. The “step” we take along the gradient is controlled by the learning rate. The smaller the value, the smaller the step, and the larger the value, the bigger the step.
- Results and discussion
- we have observed that the Random Forest Machine algorithm provides better accuracy compared to other machine learning algorithms.
- the proposed customized CNN model has a performance difference of 9% between the training and testing accuracy.
- After 150 epochs of training, the model achieved low loss with minimal overfitting. We could also improve our accuracy by adding more training data.
- We have also implemented Inception V3, a pre-trained model, and compared the accuracy with the proposed work.
- Even though there is not much difference in the accuracy, the proposed CNN model has computationally less overhead in terms of total training time as compared to the InceptionV3 model due to more layers in the network.
- Conclusion and future work
- The results show that the customized CNN has obtained an accuracy of 95.18%, which is better than the proposed machine learning algorithms.

https://www.nature.com/articles/s41598-022-22644-9#Tab7



E pluribus unum interpretable convolutional neural networks

14 July 2023

- 