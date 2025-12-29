import streamlit as st
import joblib
import pandas as pd
from PIL import Image



st.markdown(f"# :blue[PM INTENSHIP RECOMMANDATION SYSTEM]")
dataset=joblib.load("dataset")
#st.dataframe(dataset)
dp=dataset["Internship_Title"].value_counts()
dq=dataset["Skills"].value_counts()

similarity=joblib.load("similarity")
option=st.selectbox("SELECT COURSE",options=dp.index)
language=st.selectbox("SELECT YOUR SKILLS",options=dq.index)
location=st.selectbox("SELECT YOUR LOCATION",options=dataset["Location"].unique())
def recom(inten):
    index=dataset[(dataset["Internship_Title"] == inten) & (dataset["Skills"] == language) & (dataset["Location"]==location)].index[0]
    d=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
    poster=[]
    movie=[]
    ind=[]
    for i in d:
        movie.append(dataset.iloc[i[0]].Internship_Title)
        poster.append(dataset.iloc[i[0]].poster)
        ind.append(dataset.iloc[i[0]].Internship_ID)
    return movie,poster,ind

if st.button("RECOMMAND"):
    movie,poster,indexs =recom(option)
    
    
    
    
    st.markdown(f"## :orange[{movie[0]}]")
    st.image(poster[0],width=500)
    with st.expander("MORE DETAILS"):
        st.markdown(f"### :blue[INFORMATION FOR {movie[0]} INTENSHIP]")
        df=dataset[dataset["Internship_ID"]==indexs[0]]
        st.write(f"COMPANY NAME   :-  {df.iloc[0].Company}")
        st.write(f"LOCATION   :-   {df.iloc[0].Location}")
        st.write(f"SKILLS   :-   {df.iloc[0].Skills}")
        st.write(f"MODE   :-   {df.iloc[0].Mode}")
        st.write(f"SECTOR   :-   {df.iloc[0].Sector}")
    st.markdown(f"## :orange[{movie[1]}]")
    st.image("https://colleges18.s3.ap-south-1.amazonaws.com/PM_Internship_a4ae03f830.jpg",width=500)
       
    with st.expander("MORE DETAILS"):
        st.markdown(f"### :blue[INFORMATION FOR {movie[1]} INTENSHIP]")
        df=dataset[dataset["Internship_ID"]==indexs[1]]
        st.write(f"COMPANY NAME   :-  {df.iloc[0].Company}")
        st.write(f"LOCATION   :-   {df.iloc[0].Location}")
        st.write(f"SKILLS   :-   {df.iloc[0].Skills}")
        st.write(f"MODE   :-   {df.iloc[0].Mode}")
        st.write(f"SECTOR   :-   {df.iloc[0].Sector}")
    st.markdown(f"## :orange[{movie[2]}]")
    st.image("https://www.studyiq.com/articles/wp-content/uploads/2024/10/04190817/Prime-Ministers-Internship-Scheme-blog.png",width=500)
    with st.expander("MORE DETAILS"):
        st.markdown(f"### :blue[INFORMATION FOR {movie[2]} INTENSHIP]")
        df=dataset[dataset["Internship_ID"]==indexs[2]]
        st.write(f"COMPANY NAME   :-  {df.iloc[0].Company}")
        st.write(f"LOCATION   :-   {df.iloc[0].Location}")
        st.write(f"SKILLS   :-   {df.iloc[0].Skills}")
        st.write(f"MODE   :-   {df.iloc[0].Mode}")
        st.write(f"SECTOR   :-   {df.iloc[0].Sector}")
    st.markdown(f"## :orange[{movie[3]}]")
    st.image("https://vajiramandravi.com/current-affairs/wp-content/uploads/2025/07/PM_Internship_Scheme_2025_7e0829ee6b.webp",width=500)
    with st.expander("MORE DETAILS"):
        st.markdown(f"### :blue[INFORMATION FOR {movie[3]} INTENSHIP]")
        df=dataset[dataset["Internship_ID"]==indexs[3]]
        st.write(f"COMPANY NAME   :-  {df.iloc[0].Company}")
        st.write(f"LOCATION   :-   {df.iloc[0].Location}")
        st.write(f"SKILLS   :-   {df.iloc[0].Skills}")
        st.write(f"MODE   :-   {df.iloc[0].Mode}")
        st.write(f"SECTOR   :-   {df.iloc[0].Sector}")