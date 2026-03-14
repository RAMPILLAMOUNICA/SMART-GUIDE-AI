 💻 Smart Guide  AI Laptop Recommendation System

 📌 Project Overview

Smart Guide is an AI-powered laptop recommendation system that helps users choose the best laptop based on their preferences. The system asks users about their budget, preferred brand, processor, RAM, storage, and graphics, then uses a machine learning model to recommend suitable laptops.

 🚀 Features

* AI-based laptop recommendations
* User-friendly web interface built with Streamlit
* Machine learning model using Nearest Neighbors
* Filters laptops based on user preferences
* Displays top recommended laptops

 🧠 Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Machine Learning (Nearest Neighbors Algorithm)

 ⚙️ How It Works

1. User enters laptop preferences.
2. System encodes categorical features.
3. A Nearest Neighbors model compares user input with laptop dataset.
4. The system recommends the closest matching laptops.

 📂 Project Structure

```
smart-guide/
│
├── smart_guide_app.py
├── laptop_pred.csv
├── requirements.txt
└── README.md
```

 ▶️ Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run smart_guide_app.py
```

Open in browser:

```
http://localhost:8501
```

 🔮 Future Improvements

* Add mobile and other gadget recommendations
* Include laptop images
* Deploy as a public web application
* Integrate real-time product data

 👩‍💻 Author

Developed by Rampilla Mounica Siva Sai as part of an AI/ML academic project.
