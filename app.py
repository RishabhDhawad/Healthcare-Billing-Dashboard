import streamlit as st
import pandas as pd

# Title
st.title("Healthcare Billing Dashboard")

# Load Data
billing_df = pd.read_csv('billing.csv')
appointments_df = pd.read_csv('appointments.csv')
doctors_df = pd.read_csv('doctors.csv')
patients_df = pd.read_csv('patients.csv')
treatments_df = pd.read_csv('treatments.csv')

st.subheader("Billing Data Preview")
st.dataframe(billing_df.head())

# 1. Total Billing Amount
st.subheader("1. Total Billing Amount")
total_amount = billing_df['amount'].sum()
st.metric("Total Billing Amount", f"₹{total_amount:,.2f}")

# 2. Billing by Payment Method
st.subheader("2. Total Billing Amount by Payment Method")
payment_method_summary = billing_df.groupby('payment_method')['amount'].sum().reset_index()
st.dataframe(payment_method_summary)

# Optional: Show count by payment method
st.write("**Payment Method Counts**")
payment_method_counts = billing_df['payment_method'].value_counts().reset_index()
payment_method_counts.columns = ['payment_method', 'count']
st.dataframe(payment_method_counts)

# 3. Payments Status Summary
st.subheader("3. Payments Status Summary")
status_amounts = billing_df.groupby('payment_status')['amount'].sum().reset_index()
status_counts = billing_df['payment_status'].value_counts().reset_index()
status_counts.columns = ['payment_status', 'count']

st.write("**Amount by Payment Status**")
st.dataframe(status_amounts)

st.write("**Count by Payment Status**")
st.dataframe(status_counts)

# 4. List out all the patient names whose payment is either failed or pending (using two tables)
st.subheader("4. Patient Names with Failed or Pending Payments (using two tables)")
billing_df['patient_id'] = billing_df['patient_id'].astype(str).str.strip()
patients_df['patient_id'] = patients_df['patient_id'].astype(str).str.strip()
filtered_bill = billing_df[billing_df['payment_status'].isin(['Failed', 'Pending'])]
merged_df2 = pd.merge(filtered_bill, patients_df, on='patient_id', how='inner')
patient_names = merged_df2[['first_name', 'last_name']].drop_duplicates()
st.dataframe(patient_names)

# Appointment File Analysis
st.subheader("Appointment File Analysis")

# Show preview
df2_preview = appointments_df.head()
st.write("**Appointments Data Preview**")
st.dataframe(df2_preview)

# 1. Total number of appointments
st.write("**Total Number of Appointments**")
total_appointments = appointments_df['appointment_id'].nunique()
st.metric("Total Unique Appointments", total_appointments)
st.write(f"There are {total_appointments} unique appointments in the data.")

# 2. Total number of appointments based on status
st.write("**Appointments by Status**")
status_counts = appointments_df['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']
st.dataframe(status_counts)
st.write("**Appointments by Status (groupby)**")
st.dataframe(appointments_df.groupby('status').size().reset_index(name='count'))

# 3. Total number of appointments based on reason_for_visit
st.write("**Appointments by Reason for Visit**")
reason_counts = appointments_df['reason_for_visit'].value_counts().reset_index()
reason_counts.columns = ['reason_for_visit', 'count']
st.dataframe(reason_counts)
st.write("**Appointments by Reason for Visit (groupby)**")
st.dataframe(appointments_df.groupby('reason_for_visit').size().reset_index(name='count'))

# 4. Appointments before and after 3pm
st.write("**Appointments Before and After 3pm**")
appointments_df['appointment_time'] = pd.to_datetime(appointments_df['appointment_time'], format='%H:%M:%S')
before_3pm = appointments_df[appointments_df['appointment_time'].dt.hour < 15]
after_3pm = appointments_df[appointments_df['appointment_time'].dt.hour > 15]
st.write(f"Appointments before 3pm: {before_3pm.shape[0]}")
st.dataframe(before_3pm)
st.write(f"Appointments after 3pm: {after_3pm.shape[0]}")
st.dataframe(after_3pm)

# --- Billing File Analysis ---
st.subheader("Billing File Analysis")

# Show preview
st.write("**Billing Data Preview**")
st.dataframe(billing_df.head())

# 1. Find out the total billing amount
st.write("**Total Billing Amount**")
total_billing = billing_df['amount'].sum()
st.metric("Total Billing Amount", f"₹{total_billing:,.2f}")

# 2. Find out the total billing amount with different payment method
st.write("**Billing Amount by Payment Method**")
st.dataframe(billing_df.groupby('payment_method')['amount'].sum().reset_index())
st.write("**Payment Method Counts**")
payment_method_counts = billing_df['payment_method'].value_counts().reset_index()
payment_method_counts.columns = ['payment_method', 'count']
st.dataframe(payment_method_counts)
st.write("**Payment Method Group Size**")
st.dataframe(billing_df.groupby('payment_method').size().reset_index(name='count'))

# 3. Find out how many payments are Failed and Pending
st.write("**Payments by Status (Amount)**")
st.dataframe(billing_df.groupby('payment_status')['amount'].sum().reset_index())

payment_status_counts = billing_df['payment_status'].value_counts().reset_index()
payment_status_counts.columns = ['payment_status', 'count']
st.dataframe(payment_status_counts)

# Using isin
failed_and_pending = billing_df[billing_df['payment_status'].isin(['Failed','Pending'])]
st.write("**Failed and Pending Payment Status Counts**")
failed_and_pending_counts = failed_and_pending['payment_status'].value_counts().reset_index()
failed_and_pending_counts.columns = ['payment_status', 'count']
st.dataframe(failed_and_pending_counts)

# Excluding Paid category (~)
excluding_paid = billing_df[~billing_df['payment_status'].isin(['Paid'])]
st.write("**Non-Paid Payment Status Counts**")
excluding_paid_counts = excluding_paid['payment_status'].value_counts().reset_index()
excluding_paid_counts.columns = ['payment_status', 'count']
st.dataframe(excluding_paid_counts)

# 4. List out all the patient names whose payment is either failed or pending (using two tables)
st.write("**Patient Names with Failed or Pending Payments (using two tables)**")
filtered_bill = billing_df[billing_df['payment_status'].isin(['Failed','Pending'])]
merged_df2 = pd.merge(filtered_bill, patients_df, on='patient_id', how='inner')
patient_name = merged_df2[['first_name', 'last_name']].drop_duplicates()
st.dataframe(patient_name)

# ANOTHER APPROACH
st.write("**Patient Names with Failed or Pending Payments (Merge + Filter)**")
merged = pd.merge(billing_df, patients_df, on='patient_id')
result = merged[merged['payment_status'].isin(['Failed', 'Pending'])]
st.dataframe(result[['first_name', 'last_name']].drop_duplicates())

# --- Appointment File Analysis (again, for completeness) ---
st.subheader("Appointment File Analysis (Additional)")

# Show preview
st.write("**Appointments Data Preview**")
st.dataframe(appointments_df.head())

# 1. Total number of appointments
st.write("**Total Number of Appointments**")
total_appointments = appointments_df['appointment_id'].nunique()
st.metric("Total Unique Appointments", total_appointments)
st.write(f"There are {total_appointments} unique appointments in the data.")

# 2. Find the total number of appointments based on status
st.write("**Appointments by Status (value_counts)**")
appointments_status_counts = appointments_df['status'].value_counts().reset_index()
appointments_status_counts.columns = ['status', 'count']
st.dataframe(appointments_status_counts)
st.write("**Appointments by Status (groupby)**")
st.dataframe(appointments_df.groupby('status').size().reset_index(name='count'))

# 3. Find the total number of appointments based on the reason_for_visit
st.write("**Appointments by Reason for Visit (value_counts)**")
appointments_reason_counts = appointments_df['reason_for_visit'].value_counts().reset_index()
appointments_reason_counts.columns = ['reason_for_visit', 'count']
st.dataframe(appointments_reason_counts)
st.write("**Appointments by Reason for Visit (groupby)**")
st.dataframe(appointments_df.groupby('reason_for_visit').size().reset_index(name='count'))

# 4. List out all the appointments which are done before 3pm and after 3 pm
st.write("**Appointments Before and After 3pm (again)**")
appointments_df['appointment_time'] = pd.to_datetime(appointments_df['appointment_time'], format='%H:%M:%S')
before_3pm = appointments_df[appointments_df['appointment_time'].dt.hour < 15]
after_3pm = appointments_df[appointments_df['appointment_time'].dt.hour > 15]
st.write(f"Appointments before 3pm: {before_3pm.shape[0]}")
st.dataframe(before_3pm)
st.write(f"Appointments after 3pm: {after_3pm.shape[0]}")
st.dataframe(after_3pm)

# --- Patients File Analysis ---
st.subheader("Patients File Analysis")

# Show preview
st.write("**Patients Data Preview**")
st.dataframe(patients_df.head())

# 1. Find out the total number of patients
st.write("**Total Number of Patients**")
total_patients = patients_df['patient_id'].count()
st.metric("Total Patients", total_patients)

# 2. Find out how many male and female patients
st.write("**Gender Counts**")
gender_counts = patients_df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']
st.dataframe(gender_counts)
st.write("**Gender Group Size**")
st.dataframe(patients_df.groupby('gender').size().reset_index(name='count'))

# 3. List out the Patients with age range
st.write("**Patients by Age Range**")
# Try both date formats for robustness
try:
    patients_df['date_of_birth'] = pd.to_datetime(patients_df['date_of_birth'], format='%d-%m-%y')
except Exception:
    patients_df['date_of_birth'] = pd.to_datetime(patients_df['date_of_birth'])
# Calculating Age
today = pd.to_datetime('today')
patients_df['age'] = (today - patients_df['date_of_birth']).dt.days // 365
# Defining Age Range
bins = [0, 10, 20, 30, 40, 50, 60, 70, float('inf')]
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '70+']
# Create age group
patients_df['age_group'] = pd.cut(patients_df['age'], bins=bins, labels=labels)
# Group and list patient Names
age_grouped = patients_df.groupby('age_group')['first_name'].apply(list).reset_index()
st.dataframe(age_grouped)

# --- Doctors File Analysis ---
st.subheader("Doctors File Analysis")

# Show preview
st.write("**Doctors Data Preview**")
st.dataframe(doctors_df.head())

# 1. Who is the most experienced doctor?
st.write("**Most Experienced Doctor(s)**")
most_experienced = doctors_df[doctors_df['years_experience'] == doctors_df['years_experience'].max()]
st.dataframe(most_experienced[['first_name', 'last_name', 'years_experience']])

# 2. Group doctors by specialization
st.write("**Doctors by Specialization**")
specialization_counts = doctors_df['specialization'].value_counts().reset_index()
specialization_counts.columns = ['specialization', 'count']
st.dataframe(specialization_counts)

# --- Treatments File Analysis ---
st.subheader("Treatments File Analysis")

# Show preview
st.write("**Treatments Data Preview**")
st.dataframe(treatments_df.head())

# 1. Which is the most expensive treatment?
st.write("**Most Expensive Treatment**")
max_cost = treatments_df['cost'].max()
most_expensive = treatments_df[treatments_df['cost'] == max_cost][['treatment_type', 'cost']]
st.dataframe(most_expensive)

# 2. Which is the least expensive treatment?
st.write("**Least Expensive Treatment**")
min_cost = treatments_df['cost'].min()
least_expensive = treatments_df[treatments_df['cost'] == min_cost][['treatment_type', 'cost']]
st.dataframe(least_expensive)
