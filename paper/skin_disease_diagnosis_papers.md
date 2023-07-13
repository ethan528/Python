Dermatologist vs Neural Network
15 Jun 2020

HAM 10000 dataset which offers 10015 images belonging to 7 classes of ckin disease
9013 images as the training set and 1002 images as the validation set
data augmentation increases the size of dataset hence it also helps in reducing overfitting
categorical cross-entropy loss function
Adam has β1 and β2 as hyper-parameters
For training our model we have set β1 = 0.9 and β2 = 0.999.
start at alearning rate of 0.001 and it is decayed by a factor of 10 each time the validation loss plateaus after an epoch
pick the model with the lowest validation loss in this process
batch size used is 90 images
The precision, recall and f1 score of each class was impressive enough to outshine the models based on Transfer Learning
The Training accuracy achieved is 93% while the validation accuracy achieved is 89%
the model we built is far better or as good as ResNet50, InceptionV3, Vgg19, and MobileNetV2

https://paperswithcode.com/paper/dermatologist-vs-neural-network

SkinGPT-4: An Interactive Dermatology Diagnostic System with Visual Large Language Model
8 Jun 2023

SkinGPT-4 leverages a fine-tuned version of MiniGPT-4, trained on an extensive collection of skin disease images (comprising 52,929 publicly available and proprietary images) along with clinical concepts and doctors’ notes
In the initial step, SkinGPT-4 aligns visual and textual clinical concepts, enabling it to recognize medical features within skin disease images and express those medical features with natural language. In the subsequent step, SkinGPT 4 learns to accurately diagnoses the specific types of skin diseases. This comprehensive training methodology ensures the system’s proficiency in analyzing and classifying various skin conditions
Our datasets include two public datasets and our private in-house dataset, where the first public dataset was used for the step 1 training, and the second public dataset and our in-house dataset were used for the step 2 training
The first public dataset named SKINCON is the first medical dataset densely annotated by domain experts to provide annotations useful across multiple disease processes
The second public dataset named the Dermnet contains 18,856 images, which are further classified into 15 classes by our board-certified dermatologists
Our private in-house dataset contains 30,187 pairs of skin disease images and corresponding doctors’ descriptions
The training and inference procedures were conducted on a workstation equipped with 252 GB RAM, 112 CPU cores, and two NVIDIA V100 GPUs, which provided the computational resources necessary for efficient model training and inference.
prompts:
1. Could you describe the skin disease in this image for me?
2. Please provide a paragraph listing additional features you observed in the image.
3. Based on the previous information, please provide a detailed explanation of the cause of this skin disease.
4. What treatment and medication should be recommended for this case?
