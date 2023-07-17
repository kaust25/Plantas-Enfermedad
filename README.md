# Plant Disease Detection

This is an end-to-end project for plant disease detection using deep learning techniques. The project utilizes a Flask web application to allow users to upload images of plant leaves and detect diseases present in the plants. The key components of the project are as follows:

## Files

1. **app.py**: This file contains the Flask application code responsible for handling routing, image uploading, and disease detection. It uses a pre-trained convolutional neural network (CNN) model to classify the uploaded leaf images. The model was trained using transfer learning techniques on the Plant Village dataset.

2. **model.py**: This file contains the code for the plant disease detection model. It loads a pre-trained CNN model that has been fine-tuned on the Plant Village dataset. The model takes the uploaded leaf images as input and predicts the corresponding plant disease.

3. **mail.py**: This file handles sending confirmation emails to users who provide feedback through the application. It uses the `smtplib` library to send emails using a Gmail account.

## Setup

To run the project locally, follow these steps:

1. Install the required Python packages listed in the `requirements.txt` file.

2. Run the Flask application by executing the command `python app.py`.

3. Access the web application by opening `http://localhost:5000` in a web browser.

## Usage

1. Home Page: The landing page of the application.

2. Detect Page: Upload an image of a plant leaf and select the plant type. The application will detect the disease present in the leaf and display the result.

3. Feedback Page: Users can provide feedback and suggestions through this page. They will receive a confirmation email after submitting the feedback.

4. FAQ Page: Frequently Asked Questions about the application.

5. Admin Page: An admin login page to view the feedback submitted by users.


## Database

The project utilizes a SQLite database to store user feedback. The `Usr_feedback` table is created using SQLAlchemy, and it includes columns for the user's name, email, feedback, and the submission date. This allows for easy management and retrieval of user feedback.

## Deep Learning and Transfer Learning

The project leverages transfer learning to utilize the pre-trained CNN model, which has been trained on a large dataset. This approach allows the model to leverage knowledge learned from the large dataset and apply it to the task of plant disease detection. By fine-tuning the pre-trained model on the Plant Village dataset, the model can accurately classify the uploaded leaf images.

## Data Credits

The project utilizes the Plant Village dataset, which is a publicly available dataset for plant disease detection. The dataset consists of images of diseased and healthy plant leaves, along with corresponding labels. This dataset plays a crucial role in training the deep learning model to accurately classify the plant diseases. Proper credits and acknowledgments are given to the Plant Village dataset for their valuable contribution to the project.

## Low Latency Image Processing

The project is designed to efficiently process low-latency images. By leveraging the power of the pre-trained CNN model and implementing efficient image processing techniques, the application can provide quick and accurate results for disease detection. This ensures a seamless user experience, allowing for swift analysis and diagnosis of plant diseases.

---

Please note that this project is for educational purposes and should not replace professional agricultural advice. It serves as a tool to assist in the detection and identification of plant diseases, aiding in timely decision-making and effective crop management.
