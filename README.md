# 💬 AI-Powered Sentiment Analysis System

An NLP-based machine learning application that analyzes customer reviews and classifies their sentiment as **Positive, Negative, or Neutral**. The application uses a trained scikit-learn pipeline and Streamlit to provide interactive sentiment predictions with confidence scores.

## 🚀 Features

- **Sentiment Classification:** Classifies reviews into Positive, Negative, and Neutral categories.
- **Text Processing:** Uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert text into numerical features.
- **Machine Learning:** Uses a trained scikit-learn pipeline for predictions.
- **Confidence Score:** Displays the model's highest predicted class probability as a confidence score.
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
- Matplotlib and Seaborn (for exploratory data analysis and visualizations)

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

## ⚙️ How It Works

1. The user enters a customer review in the Streamlit application.
2. The trained pipeline transforms the review into TF-IDF features.
3. The machine learning classifier predicts the sentiment.
4. The application displays the predicted sentiment and the highest predicted class probability.

## 📋 Example Predictions

The following examples illustrate the types of reviews the application can analyze. Predictions and confidence scores should be verified using the trained model.

| Customer Review | Expected Sentiment |
|---|---|
| The product works perfectly and feels well made. | Positive |
| The service was disappointing and the staff were not helpful. | Negative |
| The product comes with a charging adapter and a short cable. | Neutral |

*Actual predictions depend on the trained model and its learned patterns.*

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the URL with your GitHub repository URL.

### 2. Navigate to the project directory

```bash
cd AI-Powered-Sentiment-Analysis-System
```

### 3. Create a virtual environment (recommended)

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

Ensure this file exists before running the application. The saved pipeline contains the trained text-processing and classification components.

## 📊 Model Development

The model development workflow in the Jupyter notebook covers:

- Dataset inspection and data cleaning
- Exploratory data analysis
- Text preprocessing
- TF-IDF feature extraction
- Comparison of machine learning classifiers
- Model evaluation using accuracy, precision, recall, and F1-score
- Cross-validation and hyperparameter tuning
- Saving the trained pipeline for reuse

Refer to the notebook for the actual evaluation results and implementation details.

## 🔮 Future Improvements

- Improve performance on reviews containing unfamiliar words and expressions.
- Evaluate the model on representative, previously unseen reviews.
- Improve the user interface and display class-wise prediction probabilities.
- Deploy the application online.
- Add additional evaluation visualizations and error analysis.

## 👩‍💻 Author

**Your Name**

- GitHub: [Your GitHub Profile](https://github.com/YOUR-USERNAME)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/)

## 📄 License

Add a license only if you have the right to distribute the project under that license. If this project uses company-provided data or code, follow your company's sharing and confidentiality requirements before publishing it.
