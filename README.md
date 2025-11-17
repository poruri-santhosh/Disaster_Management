# 🌊 Disaster Management Watch: AI-Powered Predictive System

This repository contains the code for an AI-powered disaster management system designed to predict and monitor high-risk zones for floods and storms, providing early warnings via a mobile-first dashboard.

This project showcases expertise in the full data science lifecycle, from data processing using Python to deploying a responsive visualization interface.

---

## ✨ Features

- **AI-Powered Prediction**: Uses a Random Forest Classifier (or similar ML model) to calculate the probability of high-risk flood or storm events.  
- **Data Pipeline**: Processes simulated environmental and satellite data (`locations.csv`) using Python (Pandas, NumPy) for feature engineering and prediction generation.  
- **Real-time Visualization**: Responsive, mobile-first dashboard (`index.html`) visualizes risk levels on an interactive map (Leaflet.js) and a categorized list.  
- **Early Warning System**: UI immediately highlights critical zones and recommends action based on ML output.

---

## 🛠️ Technology Stack

| Component          | Technology                 | Role                                                                 |
|-------------------|---------------------------|----------------------------------------------------------------------|
| Data Processing/ML | pandas, NumPy, scikit-learn | Data cleaning, feature engineering, model training, and predictions (`model.ipynb`, `train_and_predict.py`). |
| Backend/API        | Flask (Python)            | Serves the web application and exposes `predictions.json` via a REST endpoint (`app.py`). |
| Frontend/UI        | HTML, CSS, JavaScript      | Implements mobile-first dashboard and dynamic display of risk data (`index.html`, `script.js`, `styles.css`). |
| Visualization      | Leaflet.js                 | Interactive mapping to plot predicted risk zones (used within `script.js`). |

---

## 📂 Project Structure

| File                 | Purpose                                                                 | Resume Alignment                         |
|---------------------|-------------------------------------------------------------------------|-----------------------------------------|
| `model.ipynb`        | ML Core: Data loading, feature creation (e.g., Weighted Disaster Score), training, and evaluation | Python (pandas, NumPy)                  |
| `train_and_predict.py` | Production script version of the ML pipeline, generates `predictions.json` | Python (pandas, NumPy)                  |
| `predictions.json`   | JSON output containing final risk probabilities and action recommendations | Processed Data/Model Output             |
| `index.html`         | Main dashboard structure, loading CSS/JS/Map libraries                  | Mobile-first UI                          |
| `styles.css`         | Custom CSS for aesthetics and responsive design                         | Mobile-first UI with CSS                 |
| `script.js`          | Fetches `predictions.json`, handles map rendering (Leaflet), and dynamic list updates | JavaScript DOM manipulation             |
| `app.py`             | Simple Flask server for running the application locally                 | Deployment/System Development            |
| `requirements.txt`   | Python dependencies                                                      | Project Documentation                     |

---

## 🚀 Setup and Run Locally

These steps assume you have Python installed (`python3` and `pip`).

### 1. Backend Setup
Clone the repository (if applicable) and install dependencies:

```bash
# Clone the repository
# git clone [repo_url]

# Navigate to the project folder
cd [repo_folder]

# Install necessary Python libraries
pip install -r requirements.txt
2. Generate Predictions
Run the ML script to process the data and generate predictions.json:

bash
Copy code
python train_and_predict.py
3. Start the Web Server
Start the Flask application to host the dashboard:

bash
Copy code
python app.py
The application will typically run on:
http://127.0.0.1:5000/ or http://localhost:5000/

4. View the Dashboard
Open your web browser and navigate to the local host address provided by Flask to view the live risk monitoring dashboard.

yaml
Copy code

---

If you want, I can also make a **more concise, visually appealing version** that uses badges, emojis, and collapsible
