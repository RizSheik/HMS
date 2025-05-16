import streamlit as st

# ---- Stylish CSS ----
st.markdown("""
<style>
    .main {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    h1, h2, h3 {
        color: #0077b6;
        text-align: center;
    }
    .stButton>button {
        background-color: #0077b6;
        color: white;
        padding: 0.6em 2em;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        transition: background-color 0.3s ease;
        border: none;
    }
    .stButton>button:hover {
        background-color: #023e8a;
        transform: scale(1.05);
    }
    .sidebar .sidebar-content {
        background-color: #caf0f8;
    }
    .css-1v0mbdj.ef3psqc12 {
        background-color: #f1f1f1;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ---- Data Classes ----
class Doctor:
    def __init__(self, name, specialty, experience):
        self.name = name
        self.specialty = specialty
        self.experience = experience

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def remove_doctor(self, doctor_name):
        self.doctors = [d for d in self.doctors if d.name.lower() != doctor_name.lower()]

    def search_doctor(self, name):
        for doc in self.doctors:
            if doc.name.lower() == name.lower():
                return doc
        return None

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient_name):
        self.patients = [p for p in self.patients if p.name.lower() != patient_name.lower()]

    def patient_count(self):
        return len(self.patients)

# ---- App State Initialization ----
if 'hospital' not in st.session_state:
    st.session_state.hospital = Hospital("City Hospital")

hospital = st.session_state.hospital

# ---- App UI ----
st.title("🏥 Hospital Management System")
st.subheader("✨ Manage Doctors & Patients with Style")

menu = st.sidebar.radio("📋 Select Option", (
    "➕ Add Doctor", "➕ Add Patient", 
    "👨‍⚕️ Show All Doctors", "👨‍🦱 Show All Patients", 
    "🔍 Search Doctor", "🧮 Total Patients Count", 
    "❌ Remove Doctor", "❌ Remove Patient"
))

if menu == "➕ Add Doctor":
    st.header("➕ Add Doctor")
    name = st.text_input("Doctor Name")
    specialty = st.text_input("Specialty")
    experience = st.number_input("Experience (years)", min_value=0, step=1)
    if st.button("Add Doctor"):
        hospital.add_doctor(Doctor(name, specialty, experience))
        st.success(f"✅ Doctor '{name}' added successfully.")

elif menu == "➕ Add Patient":
    st.header("➕ Add Patient")
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, step=1)
    disease = st.text_input("Disease")
    if st.button("Add Patient"):
        hospital.add_patient(Patient(name, age, disease))
        st.success(f"✅ Patient '{name}' added successfully.")

elif menu == "👨‍⚕️ Show All Doctors":
    st.header("👨‍⚕️ List of Doctors")
    if hospital.doctors:
        for doc in hospital.doctors:
            st.markdown(f"✅ **{doc.name}** — *{doc.specialty}*, {doc.experience} yrs")
    else:
        st.info("No doctors added yet.")

elif menu == "👨‍🦱 Show All Patients":
    st.header("👨‍🦱 List of Patients")
    if hospital.patients:
        for pat in hospital.patients:
            st.markdown(f"🧾 **{pat.name}**, Age: {pat.age}, Disease: {pat.disease}")
    else:
        st.info("No patients added yet.")

elif menu == "🔍 Search Doctor":
    st.header("🔍 Search Doctor by Name")
    
    search_name = st.text_input("Enter doctor's name to search:")
    if search_name and st.button("Search"):

        result = hospital.search_doctor(search_name)
        if result:
            st.success(f"🔍 Found: {result.name} — {result.specialty}, {result.experience} yrs")
        else:
            st.error("❌ Doctor not found.")

elif menu == "🧮 Total Patients Count":
    st.header("🧮 Total Patient Count")
    count = hospital.patient_count()
    st.info(f"📊 Total number of patients: **{count}**")

elif menu == "❌ Remove Doctor":
    st.header("❌ Remove Doctor")
    name = st.text_input("Enter doctor name to remove:")
    if st.button("Remove"):
        hospital.remove_doctor(name)
        st.warning(f"🗑️ Doctor '{name}' removed (if existed).")

elif menu == "❌ Remove Patient":
    st.header("❌ Remove Patient")
    name = st.text_input("Enter patient name to remove:")
    if st.button("Remove"):
        hospital.remove_patient(name)
        st.warning(f"🗑️ Patient '{name}' removed (if existed).")