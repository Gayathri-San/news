## **DEEP LEARNING BASED FAKE NEWS DETECTION UISNG LSTM MODEL**

### **PROBLEM STATEMENT**
The spread of fake news online misleads the public and undermines trust,there is a need for an automated system that can detect and classify news into real or fake .

### **OBJECTIVE**
To develop an LSTM-based model that can classify news articles as real or fake to reduce spread of misinformation by providing a automated verification tool.

### **PROJECT WORKFLOW**
<p align="left">
<img width="350" height="300" alt="image" src="https://github.com/user-attachments/assets/771df46b-39d4-4e06-be07-e0e67caf165c" />

### **DATASET**
- The dataset is collected from Kaggle, a widely used platform for machine learning datasets 
- It contains a total of 51,233 news records, providing a large amount of data for training 
- The dataset consists of 3 columns such as  Title, Text ,Label 
- The large size of the dataset helps the model learn better patterns and improve prediction accuracy 
- Before training, the dataset undergoes preprocessing steps such as cleaning and formatting

### **TOOLS USED**
- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib / Seaborn

### **DATA PREPROCESSING**
- Unnecessary columns were removed to keep only relevant features for the model. 
- Text were converted to lowercase to maintain consistency and improve text quality. 
- Applied tokenization to split text into words 
- Converted text into numerical format using tokenizer and transformed it into sequences.
- Padding was applied to ensure all input sequences have equal length. 
- Split the dataset into training and testing sets for model building and evaluation

### **MODEL ARCHITECTURE**
- **INPUT LAYER**     : The input layer accepts padded sequential data, organizes it into a defined shape and passes it to the LSTM layer, where pattern     extraction take place for processing.
- **EMBEDDING LAYER** : The embedding layer transforms each word vector representation, where similar words have similar values, helping the LSTM understand relationships in the sequence.
- **LSTM LAYER**      : The LSTM layer analyzes sequences by using memory cells and gating mechanisms to selectively retain important information, discard irrelevant data, and capture long-term dependencies, enabling pattern learning in sequential data.
- **DENSE LAYER**     : The dense layer receives the extracted features from the LSTM, applies activation functions to combine and transform them, and generates the final output such as predicted value of the class

### **EVALUATION METRICS**
- **Accuracy** is used to measure the overall correctness of the model predictions, representing the ratio of correctly predicted instances to total instances. 
- **Precision** measures how many predicted fake news instances are actually fake, helping to reduce false positive predictions. 
- **Recall** measures how many actual fake news instances are correctly identified, helping to reduce false negative cases. 
- **F1-Score** measures the harmonic mean of precision and recall, providing a balanced measure of model performance. 
- **Loss value** indicates how well the model is performing during training, where lower loss means better performance

### **CONFUSION MATRIX**
<p align="left">
  <img width="300" height="300" alt="cm" src="https://github.com/user-attachments/assets/86ea0b8e-f153-4c04-8de6-a30f6c33d285" />
</p>

### **CLASSIFICATION REPORT**
<p align="left">
  <img width="500" height="650" alt="cr" src="https://github.com/user-attachments/assets/9356a923-e8a3-432e-9c8e-fefa8ca60bd7" />
</p>

### **MODEL PERFORMANCE**
- The model achieved an overall accuracy of 95%, indicating strong performance on the dataset. 
- The precision is 0.97 for class 0 and 0.94 for class 1, showing that most predicted values are correct. 
- The recall is 0.94 for class 0 and 0.96 for class 1, indicating the model effectively identifies actual instances. 
- The F1-score is approximately 0.95 for both classes, providing a balanced measure of precision and recall. 
- The model was evaluated on 10,247 samples, ensuring reliable and consistent results. 

### **DEPLOYMENT**
- The trained model is deployed using Streamlit to create an interactive web application. 
- The application allows users to input news text and get instant predictions as real or fake. 
- The saved model file is loaded into the Streamlit app for prediction. 
- User input is preprocessed in the same way as training data before making predictions. 
- The system provides a simple and user-friendly interface for easy usage.

### **FUTURE WORK**
- Improve the model accuracy by using advanced techniques like BERT
- Increase dataset size and include more diverse  news data for better generalization. 
- Add support for multiple languages to detect fake news in different regions. 
- Enhance the application with real-time news verification and API integration. 
- Improve the user interface and deploy the system on cloud platforms for wider accessibility.








