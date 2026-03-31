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

### **DATA PREPROCESSING**
- Unnecessary columns were removed to keep only relevant features for the model. 
- Text were converted to lowercase to maintain consistency and improve text quality. 
- Applied tokenization to split text into words 
- Converted text into numerical format using tokenizer and transformed it into sequences.
- Padding was applied to ensure all input sequences have equal length. 
- Split the dataset into training and testing sets for model building and evaluation

### **MODEL ARCHITECTURE**
- #### **INPUT LAYER** : The input layer accepts padded sequential data, organizes it into a defined shape and passes it to the LSTM layer, where pattern extraction take place for processing.
- EMBEDDING LAYER : The embedding layer transforms each word vector representation, where similar words have similar values, helping the LSTM understand relationships in the sequence.
- LSTM LAYER : The LSTM layer analyzes sequences by using memory cells and gating mechanisms to selectively retain important information, discard irrelevant data, and capture long-term dependencies, enabling pattern learning in sequential data.
- DENSE LAYER : The dense layer receives the extracted features from the LSTM, applies activation functions to combine and transform them, and generates the final output such as predicted value of the class
- 



