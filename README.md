<!-- PROJECT BANNER -->
<!-- <p align="center"> -->
  <!-- <img src="https://img.shields.io/badge/Streamlit-Healthcare%20Billing%20Dashboard-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" alt="Healthcare Billing Dashboard"/> -->
<!-- </p> -->

<h1 align="center">🏥 Healthcare Billing Dashboard</h1>

<p align="center">
  <b>A modern, interactive Streamlit dashboard for visualizing and analyzing healthcare billing, appointments, patients, doctors, and treatments data.</b>
  <br/>
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-%E2%9C%A8%20App-red?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
</p>

---

## 🚀 Project Overview
This dashboard provides a comprehensive view of healthcare operations, including billing summaries, appointment analytics, patient demographics, doctor experience, and treatment costs. It is designed for clinics, hospitals, and healthcare analysts to gain actionable insights from their data.

---

## ✨ Features
- 💸 **Billing Analytics:**
  - Total billing amount and breakdown by payment method
  - Payment status summaries (Paid, Failed, Pending)
  - List of patients with failed or pending payments

- 📅 **Appointment Analytics:**
  - Total and unique appointment counts
  - Appointments by status and reason for visit
  - Time-based analysis (before/after 3pm)

- 👨‍⚕️ **Patient Demographics:**
  - Total patients
  - Gender distribution
  - Age group segmentation

- 🩺 **Doctor Insights:**
  - Most experienced doctor(s)
  - Doctors grouped by specialization

- 💊 **Treatment Costs:**
  - Most and least expensive treatments

---

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your data:**
   - Place your CSV files (`billing.csv`, `appointments.csv`, `doctors.csv`, `patients.csv`, `treatments.csv`) in the project root directory.
4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## 📊 Usage
- Open the Streamlit app in your browser (usually at `http://localhost:8501`)
- Explore the sidebar and main dashboard for interactive data exploration
- Filter, sort, and analyze your healthcare data visually

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
