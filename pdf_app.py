import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("Homework Assignment 01")

st.write(
    "This app converts your answers in the space provided to a pdf template that is convenient to grade in gradescope. \n So please fill the form carefully and make sure that you have pdf downloaded at the end of your work"
)

#left, right = st.columns(2)
#right.write("Here's the template we'll be using:")
st.write("Here's the template we'll be using:")
#right.image("template.png", width=300)
st.image("template.png", width=300)
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

#left.write("Fill in the data:")
st.write("Fill in the data:")
#form = left.form("template_form")
form= st.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit", "Advanced Cryptography"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    #st.balloons()

    #right.success("Your template successfully generated!")
    st.success("Your template successfully generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    #right.download_button(
    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        #file_name="diploma.pdf",
        file_name="your_name.pdf",
        mime="application/octet-stream",
    )
#This file uses the virt env at
# conda activate  C:\Users\aembaye\AppData\Local\anaconda3\venv2
# streamlit run pdf_app.py