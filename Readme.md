# 🧹 Data Cleaning App (Streamlit)

A simple and interactive **data cleaning showcase app** built with **Python, Pandas, and Streamlit**.  
This project demonstrates how raw data can be transformed into a clean, structured format using common data preprocessing techniques.

---

## 🚀 Live Demo

👉 [Add your Streamlit app link here]

---

## 📌 Project Overview

This app is designed to **showcase data cleaning skills** in a clear and visual way.

Instead of uploading external data, the app uses a **preloaded dataset** and demonstrates:

- Raw (uncleaned) data
- Step-by-step cleaning process
- Final cleaned dataset
- Basic insights

---

## ⚙️ Features

- 📄 View original dataset  
- 🧹 Automated data cleaning pipeline  
- ✨ Cleaned dataset display  
- 📊 Basic statistical insights  
- ⬇️ Option to download cleaned data  

---

## 🧠 Data Cleaning Steps

The following preprocessing steps are applied:

- Removed duplicate rows  
- Converted numerical columns (Age, Salary)  
- Handled missing values using mean/median  
- Standardized text fields (Name, Email)  
- Cleaned and formatted date columns  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Streamlit**

---

## 📂 Project Structure

data-cleaner-app/
│
├── app.py # Streamlit app
├── data.csv # Sample dataset
├── cleaner.py # Data cleaning logic
├── requirements.txt # Dependencies
└── README.md


---

## ▶️ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/data-cleaner-app.git
cd data-cleaner-app


2. Install dependencies:

pip install -r requirements.txt

3. Run the app:

streamlit run app.py