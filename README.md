
# Crop Recommendation System

A machine learning-based web application that provides data-driven recommendations for the most suitable crop to cultivate. This system analyzes crucial soil and climate parameters, including **Nitrogen (N), Phosphorus (P), and Potassium (K) levels, temperature, humidity, pH, and rainfall**, to deliver accurate and actionable insights. Built using **Python, Flask, and scikit-learn**, this project showcases a complete end-to-end machine learning pipeline, from data preprocessing to model deployment.

---

### Key Features and Technical Highlights

* **Machine Learning Model:** Utilizes a **Random Forest Classifier**, a robust ensemble learning method, to predict the optimal crop. This model achieved an exceptional accuracy of **99.77%** on the test dataset.
* **Data Preprocessing:**
    * **Data Cleaning:** Performed extensive exploratory data analysis (**EDA**) to inspect the dataset. Confirmed zero null or duplicate values, ensuring a high-quality input for model training.
    * **Feature Scaling:** Applied **MinMaxScaler** followed by **StandardScaler** to normalize and standardize the input features. This crucial step prevents features with larger numerical ranges from disproportionately influencing the model's performance.
* **Model Training and Evaluation:**
    * Compared the performance of **10 different machine learning models** (including Logistic Regression, GaussianNB, SVC, and various ensemble methods) to identify the best-performing algorithm.
    * Used a **stratified split** to partition the dataset into training and testing sets, ensuring that the class distribution of the target variable (`label`) was consistent across both sets.
* **Scalable Web Application:**
    * Developed a user-friendly and responsive web interface using **Flask** for the backend and **HTML/CSS** for the frontend.
    * The application takes real-time user input and serves predictions efficiently.
* **Model Deployment:** The trained model and preprocessing scalers were serialized using the **`pickle`** library, enabling them to be easily loaded and used for inference in the Flask application.

---

### Project Structure

crop_recommendation_project/
│
├── app.py # Main Flask application script
├── model/ # Directory for serialized machine learning assets
│   ├── randclf_model.pkl # The trained Random Forest model
│   ├── minmax_scaler.pkl # The fitted MinMaxScaler object
│   ├── standard_scaler.pkl # The fitted StandardScaler object
│   └── label_mapping.pkl # Dictionary for mapping numerical labels back to crop names
├── templates/ # HTML templates for the web interface
├── static/ # CSS files and images for the frontend
├── notebooks/ # Jupyter notebook detailing the data analysis and model training
├── data/ # CSV dataset used for training
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

### Getting Started

#### Prerequisites

-   Python 3.7+
-   pip (Python package installer)

#### Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/yourusername/crop_recommendation_project.git](https://github.com/yourusername/crop_recommendation_project.git)
    cd crop_recommendation_project
    ```
2.  **(Optional but recommended) Create and activate a virtual environment**:
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```
3.  **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

---

### Usage

1.  **Run the Flask application**:
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000/`.
3.  Enter the required soil and environmental parameters in the form and click "Submit" to receive the crop recommendation.

---

### Methodology and Insights

The Jupyter notebook in the `notebooks/` directory provides a detailed walk-through of the entire process:

-   **Exploratory Data Analysis (EDA):** Visualizations and statistical summaries were used to understand the distribution of each feature and its relationship with the target variable.
-   **Model Selection:** The accuracy scores of various classifiers were compared, leading to the selection of the Random Forest model for its superior performance and robustness.
-   **Reproducibility:** The `random_state` parameter was set to ensure that model training and data splitting are reproducible.

---

### License

This project is open-source and available under the **MIT License**.

---

### Acknowledgments

-   Dataset sourced from **Kaggle**.
-   The **scikit-learn** team for providing powerful and easy-to-use machine learning tools.
-   **Icons8** for UI icons.

---

*Feel free to raise issues or contribute via pull requests!* 🌾🌱
