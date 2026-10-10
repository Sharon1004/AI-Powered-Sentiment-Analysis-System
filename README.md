# 💬 AI-Powered Sentiment Analysis System

An NLP-based machine learning application that analyzes customer reviews and classifies their sentiment as **Positive, Negative, or Neutral**. The application uses a trained scikit-learn pipeline and Streamlit to provide interactive sentiment predictions with confidence scores.

## 🚀 Live Demo

**Try the application:** [AI-Powered Sentiment Analysis System](https://ai-powered-sentiment-analysis-system.streamlit.app/)

Enter a customer review to see the predicted sentiment and confidence score.

## ✨ Features

- **Sentiment Classification:** Classifies customer reviews into Positive, Negative, and Neutral categories.
- **Text Processing:** Uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert text into numerical features.
- **Machine Learning:** Uses a trained scikit-learn pipeline to generate predictions.
- **Confidence Score:** Displays the highest predicted class probability.
- **Interactive Web Interface:** Allows users to enter reviews and analyze their sentiment.
- **Input Validation:** Prompts users to enter a review before analysis.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Joblib
- Matplotlib
- Seaborn

## 📂 Project Structure

```text
AI-Powered-Sentiment-Analysis-System/
│
├── app.py
├── data/
│   └── reviews.csv
├── models/
│   └── sentiment_pipeline.pkl
├── notebooks/
│   └── sentiment_analysis.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: The dataset is shown for illustration. Do not publish company-provided data unless you have permission.*

## ⚙️ How It Works

1. The user enters a customer review in the Streamlit application.
2. The trained pipeline transforms the review into TF-IDF features.
3. The machine learning classifier predicts the sentiment.
4. The application displays the predicted sentiment and its highest predicted class probability.

## 📋 Example Predictions

The following reviews demonstrate the types of inputs the application can analyze.

| Customer Review | Expected Sentiment |
|---|---|
| The product works perfectly and feels well made. | Positive |
| The service was disappointing and the staff were not helpful. | Negative |
| The product comes with a charging adapter and a short cable. | Neutral |

*These are illustrative examples, not a guarantee of model output. Run each review through the deployed application to verify its prediction and confidence score.*

## 💻 Installation and Setup

### 1. Clone the repository

Replace the URL below with your actual GitHub repository URL.

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd AI-Powered-Sentiment-Analysis-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 Trained Model

The application loads the saved model from:

```text
models/sentiment_pipeline.pkl
```

Ensure this file exists before running the application. The saved pipeline contains the trained text-processing and classification components used to generate predictions.

## 📊 Model Development and Evaluation

The Jupyter notebook documents the model development workflow, including:

- Dataset inspection and data cleaning
- Exploratory data analysis (EDA)
- Text preprocessing
- TF-IDF feature extraction
- Comparison of machine learning classifiers
- Model evaluation using accuracy, precision, recall, and F1-score
- Cross-validation and hyperparameter tuning
- Saving the trained pipeline for reuse

Refer to the notebook for the implementation details and actual evaluation results.

## 🔮 Future Improvements

- Improve performance on reviews containing unfamiliar words and expressions.
- Evaluate the model on representative, previously unseen reviews.
- Display class-wise prediction probabilities.
- Improve the user interface and user experience.
- Expand evaluation visualizations and error analysis.

## 👩‍💻 Author

**Your Name**

- **GitHub:** [Your GitHub Profile](https://github.com/Sharon1004)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/sharon-bethireddy/)

## 📄 License and Data Usage

This project uses a trained machine learning model and may involve company-provided data.

Before making the repository public, ensure you have permission to share the source code, trained model, dataset, and any company-related information. Do not include confidential data or credentials in the repository.

Add a license only if you have the right to distribute the project under that license.
