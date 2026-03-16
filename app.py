import streamlit as st
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

st.title("Student Performance Predictor")
st.write("Using a Naive Bayes algorithm to predict student performance based on evaluations.")

df = pd.read_csv('Fixed_CompleteCombi.csv')

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df = df[['Attendance', 'Study Hours', 'Assignment Score', 'Quiz Scores', 'Result']]

encoder = OrdinalEncoder()
X = encoder.fit_transform(df.drop('Result', axis=1))
y = df['Result']

model = CategoricalNB(alpha=1)
model.fit(X, y)

accuracy = model.score(X, y)
st.sidebar.title("Model Stats")
st.sidebar.metric(label="Training Accuracy", value=f"{accuracy * 100:.1f}%")
st.sidebar.info("Model trained on logical combinations data.")

st.subheader("Enter Conditions:")

col1, col2 = st.columns(2)

with col1:
    att = st.selectbox("Attendance", df['Attendance'].unique())
    sh = st.selectbox("Study Hours", df['Study Hours'].unique())

with col2:
    asc = st.selectbox("Assignment Score", df['Assignment Score'].unique())
    qs = st.selectbox("Quiz Scores", df['Quiz Scores'].unique())

st.write("---") 

if st.button("Predict Result"):
    
    feature_cols = ['Attendance', 'Study Hours', 'Assignment Score', 'Quiz Scores']
    test_data = pd.DataFrame([[att, sh, asc, qs]], columns=feature_cols)
    
    try:
        encoded_test = encoder.transform(test_data)
        prediction = model.predict(encoded_test)
        
        probabilities = model.predict_proba(encoded_test)[0]
        classes = model.classes_
        
        st.write("### Model Confidence:")
        for cls, prob in zip(classes, probabilities):
            st.write(f"- *{cls}*: {prob * 100:.1f}%")
            
        if prediction[0].upper() == "FAIL":
            st.error("PREDICTION: The student will FAIL.")
        else:
            st.success("PREDICTION: The student will PASS.")
            
    except Exception as e:
        st.error(f"Error: {e}")