from Score import score
from Score import preprocess
from similarity import calc_similarity
import streamlit as st
import os
from pdfminer.high_level import extract_text
import zipfile


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

st.header("HR Resume Tool")
uploaded_jd_file = st.file_uploader('Choose your job description (.pdf file only)', type="pdf")
if uploaded_jd_file is not None:
    jd = extract_text_from_pdf(uploaded_jd_file)
    jd = preprocess(jd)

uploaded_resumes_zip = st.file_uploader('Choose your resume dump (.zip file only)', type="zip")
if (uploaded_resumes_zip is not None):
    zf = zipfile.ZipFile(uploaded_resumes_zip)
    zf.extractall()
    scores = []
    path = os.path.join(str(uploaded_resumes_zip.name)[:len(uploaded_resumes_zip.name)-4])
    tp = os.listdir()
    for i in range(len(tp)):
        if tp[i].lower() in path:
            path = tp[i]
            break
    st.write(path)
    resumes = os.listdir(path)
    resume_score = []
    resume_tokens = []
    for resume in resumes:
        temp = os.path.join(str(uploaded_resumes_zip.name)[:len(uploaded_resumes_zip.name)-4],resume)
        resume_score.append(score(temp))
        resume_tokens.append(preprocess(extract_text_from_pdf((temp))))
    resumes_score = dict(zip(resumes,resume_score))

    resume_sim = []
    for i in resume_tokens:
        resume_sim.append(calc_similarity(jd,i))

    resumes_sim = dict(zip(resumes,resume_sim))
    st.subheader("Similarity of resumes with job descirption")
    st.write(resumes_sim)
    st.subheader("Resume attribute scoring")
    st.write(resumes_score)