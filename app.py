import streamlit as st
from fpdf import FPDF

# Streamlit App
st.title("VAT Agreement PDF Generator")

with st.form("vat_form"):
    agreement_date = st.date_input("Date of Agreement")
    attention = st.text_input("Attention")
    email = st.text_input("Email")
    client_name = st.text_input("Client Name")
    client_cr = st.text_input("Commercial Registration Number")
    service_provider = st.text_input("Service Provider Name")
    provider_cr = st.text_input("Service Provider CR Number")
    company_name = st.text_input("Company Name")
    vat_fee = st.number_input("VAT Registration Fee", min_value=0.0)
    consult_fee = st.number_input("Consultancy Fee", min_value=0.0)
    auth_person = st.text_input("Authorized Person Name")

    submitted = st.form_submit_button("Generate VAT PDF")

if submitted:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="VAT Registration Agreement", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Date of Agreement: {agreement_date}", ln=True)
    pdf.cell(200, 10, txt=f"Attention: {attention}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Client Name: {client_name}", ln=True)
    pdf.cell(200, 10, txt=f"Commercial Registration Number: {client_cr}", ln=True)
    pdf.cell(200, 10, txt=f"Service Provider Name: {service_provider}", ln=True)
    pdf.cell(200, 10, txt=f"Service Provider CR Number: {provider_cr}", ln=True)
    pdf.cell(200, 10, txt=f"Company Name: {company_name}", ln=True)
    pdf.cell(200, 10, txt=f"VAT Registration Fee: {vat_fee}", ln=True)
    pdf.cell(200, 10, txt=f"Consultancy Fee: {consult_fee}", ln=True)
    pdf.cell(200, 10, txt=f"Authorized Person Name: {auth_person}", ln=True)

    pdf_file = "vat_agreement.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download VAT Agreement PDF",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )
