import streamlit as st
import pandas as pd
import os

# Set page title
st.set_page_config(page_title="Medico-Legal Document Submission", layout="centered")

# Title and Description
st.title("📜 Medico-Legal Document Submission Form")
st.write("Please fill out the details below and upload the required documents.")

# Section 1: General Information
st.header("🔹 General Information")
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
submission_date = st.date_input("Date of Submission")

# Section 2: Document Details
st.header("🔹 Document Details")
case_ref = st.text_input("Case Reference Number")
document_type = st.selectbox("Type of Document Submitted", 
                             ["Medical Report", "Legal Notice", "Police Report", "Court Order", "Others"])
incident_date = st.date_input("Date of Incident")
hospital_name = st.text_input("Hospital/Medical Institution Name")
doctor_name = st.text_input("Doctor/Officer in Charge")

# Section 3: Document Status
st.header("🔹 Document Status")
all_fields_filled = st.radio("Are all required fields filled in the document?", ["Yes", "No"])
missing_info = st.text_area("If there are missing/unclear details, please specify:", placeholder="Mention any missing or unclear information.")

# Section 4: Supporting Evidence
st.header("🔹 Supporting Evidence")
uploaded_file = st.file_uploader("Upload Supporting Document (PDF, DOCX, or Image)", type=["pdf", "docx", "png", "jpg", "jpeg"])
document_purpose = st.text_area("Brief Description of the Document’s Purpose")

# Section 5: Verification & Consent
st.header("🔹 Verification & Consent")
verified = st.checkbox("I verify that the information provided is accurate.")
consent = st.checkbox("I consent to the use of this document for legal and investigative purposes.")

# Save Data Function
def save_data():
    data = {
        "Full Name": full_name,
        "Email": email,
        "Phone": phone,
        "Date of Submission": submission_date,
        "Case Reference Number": case_ref,
        "Document Type": document_type,
        "Date of Incident": incident_date,
        "Hospital Name": hospital_name,
        "Doctor Name": doctor_name,
        "Fields Filled": all_fields_filled,
        "Missing Info": missing_info,
        "Document Purpose": document_purpose,
        "Verified": verified,
        "Consent Given": consent
    }
    
    df = pd.DataFrame([data])
    file_exists = os.path.isfile("medico_legal_submissions.csv")
    
    # Append data to CSV file
    df.to_csv("medico_legal_submissions.csv", mode="a", header=not file_exists, index=False)

    st.success("✅ Your submission has been recorded!")

# Submit Button
if st.button("Submit"):
    if full_name and email and phone and case_ref and document_type and verified and consent:
        save_data()
    else:
        st.warning("⚠️ Please fill in all required fields and accept the consent.")

