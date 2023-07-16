# Econ 3133 News Analysis HW01
import pdfkit
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Econ 2013 News Analysis Assignment 01")
st.title("Econ 2013 News Analysis Assignment 01")


#left, right = st.columns(2)
#right.write("Here's the template we'll be using:")
#st.write("Here's the template we'll be using:")
#right.image("template.png", width=300)
# st.image("template.png", width=300)
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

#left.write("Fill in the data:")
#st.write("Fill in the data:")
#form = left.form("template_form")
form = st.form("template_form")

# ...

with form:
    student = st.text_input(label="Student name", placeholder="Abel Embaye", max_chars=70)

    # st.write("This page is an app that converts your answers in the space provided to a PDF template that is convenient to grade in Gradescope. "
    #          "Please fill in the form carefully and make sure that you are able to download a PDF file at the end of your work "
    #          "by clicking the 'Generate PDF' button and then the 'Download' button.")
    #
    # st.write("Please read the following article from the Wall Street Journal (WSJ) titled 'TSMC to Boost Chip Production With Up to $44 "
    #          "Billion Investment,' by Yang Jie, January 13, 2022 issue. "
    #          "https://www.proquest.com/docview/2619154138/123B20B55928445DPQ/1?accountid=8361")
    #
    # st.write("1. From the article: “Taiwan Semiconductor Manufacturing Co., the world’s largest contract chip maker, said it "
    #          "would increase its investment to boost production capacity by up to 47% this year from a year earlier as demand continues to "
    #          "surge amid a global chip crunch.” Firms make short-run and long-run production decisions. Is TSMC’s decision to increase production "
    #          "capacity a short-run or a long-run decision? Briefly explain your answer.")

    q01 = st.text_area("Please enter your answer for question 1.", placeholder="There is no place like Econ", height=100, max_chars=500)

    # st.write("2. Please use the following page to draw and then save a PNG file and upload it on this page: "
    #          "https://xlitemprod.pearsoncmg.com/Grapher/Grapher.aspx?productid=ccng&appproductid=4&handler_urn=pearson%2Fccng_econ_xl%2Fslink%2Fx-pearson-ccng_econ_xl&learningproduct=VL."
    #          " Draw and label a graph that depicts a downward-sloping demand curve and an upward-sloping supply curve in the "
    #          "market for semiconductor chips. Assume that the market price and quantity of semiconductor chips are equal to the equilibrium "
    #          "price and quantity. The article states: “As a pandemic-fueled surge in demand for various devices requiring semiconductors has "
    #          "created widespread shortages, major chip makers have been on an investment spree to raise production capacity.” Use your graph to depict:")
    #
    st.write("2a. How an increase in demand could result in a shortage of chips")
    img01 = st.file_uploader(label="Answer question #2a by uploading the PNG file of your drawing",type='png')
    if img01 is not None:
        st.write("Uploaded Image:")
        st.image(img01 , use_column_width=True)

submit = form.form_submit_button("Click Me to Generate PDF")

if submit:
    html = template.render(
        student=student,
        q01=q01,
        #grade=f"{grade}/100",
        img01=img01,
        #date=date.today().strftime("%B %d, %Y"),
        #img02=img02,
    )

    #pdf = pdfkit.from_string(html, False)
    #pdf = pdfkit.from_string(html, "out2.pdf", configuration=config) #remove "out.pdf" if you want to let student to upload the pdf
    #pdf = pdfkit.from_string(html , configuration=config, options={"enable-local-file-access": ""})
    pdf = pdfkit.from_string(html , False)
    st.balloons()

    #right.success("Your template successfully generated!")
    st.success("Your template successfully generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    #right.download_button(
    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        #file_name="diploma.pdf",
        file_name="your_work.pdf",
        mime="application/octet-stream",
    )
#This file uses the virt env at
#..\venv4pdfgen\Scripts\activate.ps1
#streamlit run ./pdf_app.py

# streamlit run ./diploma_app.py
