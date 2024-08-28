import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))
def predict(sl,sw,pl,pw):
    prediction=model.predict([[sl,sw,pl,pw]])
    return prediction
def main():
    st.title("Loan Prediction") 
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Loan Predictor </h2>   
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sl = st.text_input("Applicant Income","Type Here")
    sw = st.text_input("Loan Amount","Type Here")
    pl = st.text_input("Credit History","Type Here")
    pw = st.text_input("Employment Status","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(sl,sw,pl,pw)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
main()