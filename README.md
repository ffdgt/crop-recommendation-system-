# Crop Recommendation System

A machine learning-based crop recommendation web application that suggests the most suitable crop based on soil nutrients and environmental parameters. The app is built using Python, Flask, and scikit-learn, providing an an intuitive and responsive user interface for farmers and agricultural researchers.

---

### Features

- Predicts the best crop based on soil and weather features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH level, and Rainfall.
- Interactive and elegant web interface with clean design.
- Responsive layout for desktops and mobile devices.
- Uses a trained Random Forest model for predictions.
- Modular codebase with clear separation of model, templates, and static resources.
- Easy to extend and customize.

---

### Project Structure

# Crop Recommendation System

A machine learning-based crop recommendation web application that suggests the most suitable crop based on soil nutrients and environmental parameters. The app is built using Python, Flask, and scikit-learn, providing an an intuitive and responsive user interface for farmers and agricultural researchers.

---

### Features

- Predicts the best crop based on soil and weather features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH level, and Rainfall.
- Interactive and elegant web interface with clean design.
- Responsive layout for desktops and mobile devices.
- Uses a trained Random Forest model for predictions.
- Modular codebase with clear separation of model, templates, and static resources.
- Easy to extend and customize.

---

### Project Structure

crop_recommendation_project/
│
├── app.py # Flask application code
├── model/ # Pickled model and scalers
│   ├── randclf_model.pkl
│   ├── minmax_scaler.pkl
│   ├── standard_scaler.pkl
│   └── label_mapping.pkl
├── templates/ # HTML templates (index.html, result.html)
├── static/ # Static files (CSS, images - optional)
├── notebooks/ # Jupyter notebook with training and analysis
├── data/ # Dataset CSV file
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

### Getting Started

#### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

#### Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/yourusername/crop_recommendation_project.git](https://github.com/yourusername/crop_recommendation_project.git)
    cd crop_recommendation_project
    ```
2.  **(Optional but recommended) Create and activate a virtual environment**:
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
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
2.  **Open your browser** and navigate to:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```
3.  Enter the soil and environmental parameters in the form and submit to get crop recommendations.

---

### Model Training

The Random Forest model was trained on a dataset containing soil nutrient values and climate features mapped to crops.

To retrain the model or experiment with other models, open the Jupyter notebook in the `notebooks/` folder and run the cells step-by-step.

---

### License

This project is open-source and free to use under the **MIT License**.

---

### Acknowledgments

- Dataset source and contributors.
- **[Icons8](https://icons8.com)** for the beautiful icons used in the UI.
- Inspiration from various crop recommendation research and agriculture technology initiatives.

---

Feel free to raise issues or contribute via pull requests!

---

*Happy Farming!* 🌾🌱
