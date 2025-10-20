# DisasterWatch AI: Proactive Flood Risk Dashboard

## Project Overview
This project presents an AI-powered early warning system for flood risks, designed for the [Your Hackathon Name] Hackathon. It integrates:
- **Satellite Imagery Analysis:** Identifies water bodies and saturated ground.
- **Environmental Sensor Data:** Incorporates rainfall, temperature, water level, and humidity data.
- **Machine Learning:** A RandomForestClassifier predicts flood risk levels.

The dashboard aims to provide timely, data-driven insights to help communities and emergency responders mitigate the impact of floods.

## Features
- Interactive map showing historical flood-prone areas and real-time satellite-detected water.
- Dynamic flood risk level indicator (e.g., High, Medium, Low).
- Numerical overall flood risk score (0-100) with a visual meter.
- AI-generated natural language summary of the current flood situation.
- Latest environmental data display.
- Simulated flood risk trend chart.

## How to Run This Project

### Prerequisites
- Python 3.x
- Jupyter Notebook or Jupyter Lab
- All required Python libraries listed in `requirements.txt`

### Setup Steps
1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/DisasterWatch-AI-Hackathon.git](https://github.com/YOUR_GITHUB_USERNAME/DisasterWatch-AI-Hackathon.git)
    cd DisasterWatch-AI-Hackathon
    ```
    (Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username and `DisasterWatch-AI-Hackathon` with your repository name).

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook Final_Project.ipynb
    # or
    # jupyter lab Final_Project.ipynb
    ```

4.  **Execute all cells in `Final_Project.ipynb` sequentially (Cell 1, Cell 2, Cell 3).**
    - Cell 1: Processes satellite imagery, loads environmental data, prepares data for ML, trains the model, and displays data distribution plots.
    - Cell 2: Generates the interactive Folium map.
    - Cell 3: Generates the `disaster_watch_ai_dashboard.html` file with all dashboard elements.

5.  **Open the dashboard:** After running Cell 3, a file named `disaster_watch_ai_dashboard.html` will be created in your project folder. Open this file in any web browser to view the interactive dashboard.

## Data Sources
- `Satellite.jpeg.jpg`: Simulated satellite imagery for flood detection.
- `Latitude.csv`: Simulated environmental sensor data (rainfall, temperature, etc.).

## Technologies Used
- Python (Pandas, NumPy, Matplotlib, scikit-learn, OpenCV, Folium, Pillow, Joblib)
- HTML, CSS (Tailwind CSS framework)
- JavaScript (for dashboard interactivity)

---
*Developed for QUANTANOVA V1 by [Code Crafters]*
