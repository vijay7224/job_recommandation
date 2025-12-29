import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import CountVectorizer
cp=CountVectorizer(max_features=5000,stop_words="english")
from sklearn.metrics.pairwise import cosine_similarity
data=pd.read_csv(r"C:\Users\payal\Desktop\internship.csv")
data["overview"]=data["Internship_Title"]+" " +data['Location']+" "+data['Skills']+" "+['Mode']+" "+data['Sector']
dataset=data[['Internship_ID','Internship_Title','Poster url','Location','Company','overview','Skills','Mode','Sector']]
x= cp.fit_transform(dataset["overview"]).toarray()
x.shape
similarity=cosine_similarity(x)
dataset.rename(columns={'Poster url': "poster"}, inplace=True)
def recom(inten):
    index=dataset[dataset["Internship_Title"]==inten].index[0]
    d=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
    for i in d:
        print(dataset.iloc[i[0]].Internship_Title)
        print(dataset.iloc[i[0]].poster)
recom("Machine Learning")
joblib.dump(similarity,"similarity")
joblib.dump(dataset,"dataset")
