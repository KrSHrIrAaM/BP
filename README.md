BP Assignment
-
Evaluation Criteria
-
1. Correct implementation of object detection on your chosen backbone
2. Model performance on test data
3. Code quality and organization
4. Thoughtfulness of your experience report
5. Effective use of AI assistance

Additional
-
Based on these evaluation criteria, I developed two models. Initially, I planned to develop a YOLOv5 model using the COCO2017 dataset, which is around 25GB. However, this made it difficult to train the model on my laptop. Hence, I switched to a smaller dataset — the COCO128 dataset, which is around 1GB.
Using the COCO128 dataset, which consists of only training images and annotations, I split the training dataset into train and validation sets. I used YOLOv8 and PyTorch to develop the model.

Training
-
1. Initially, I downloaded the model and dataset from GitHub and split the dataset into training and validation sets.
2. I created a file called coco128_classes.yaml to define all the classes in the dataset so that the model could identify the objects based on the defined classes.
3. The next step was training the model and evaluating it.
 
Challenges Faced During Model Development [COCO128 Dataset]
-
1. The main challenge I faced was encountering many corrupted images due to incorrect class ranges.
2. Initially, the class range was from 0–9, which made the model detect only 9 objects and skip all the other training images.
Solutions to the Problems Faced
3. I added more classes (80) to my .yaml file, which resolved the issue and resulted in 0 corrupted images during training.

Evaluation Metrics
-
1. The evaluation metrics I used were Precision, Recall, mAP50, and mAP50–95.
2. The accuracy of the model was around 75% with an IoU threshold of 0.5.
3. Due to the small dataset size, the accuracy ranged between 70–75%.





Due to the limited dataset, I decided to train another model with a larger dataset. I merged the COCO128 and Pascal VOC datasets so that both training images were combined into a single folder, and their annotations were combined into another.

Challenges Faced
-
1. The main challenge was that all the annotations in the Pascal VOC dataset were in XML format.
2. Another major issue was that the classes were different in the COCO and Pascal VOC datasets, which confused the model and led to incorrect predictions.
   
Solution
-
1. I converted the XML files to TXT format.
2. Initially, I planned to map the Pascal VOC classes to the COCO classes, but I eventually converted Pascal VOC annotations to COCO format so that both used the same class IDs.
This also eliminated all corrupted images during model training.

As of now, I have only updated the files for the COCO128-based trained model, as the other model is still in training. Once completed, I will include it in the repository.
The reason for submitting this a day earlier than the original deadline is because I believe the time and effort taken to build this model should also be considered as part of the evaluation criteria.

Role of AI
-
I used GitHub Copilot and ChatGPT for assistance while developing this model. They helped me with dataset splitting, writing scripts for evaluation metrics, and resolving problems with appropriate solutions.
