import streamlit as st
import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike', 'Emily'],
        'Age': [25, 32, 45, 27],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
#print(df)


st.title("My Streamlit App")
st.write("Welcome to my Streamlit App")
st.header("this is the header")
st.subheader("this the sub header")
st.text("this is the text area")
st.markdown("this is the markdown")
st.image('qrcode0.png')
st.button("label")
st.checkbox('label1')
st.selectbox("select anyone", ["l1","l2","l3"])
st.multiselect("select anyone multi ", ["l1","l2","l3"])
st.slider("this is temp",0,100)
st.date_input("please enter you DOP")
st.time_input("enter the time")
st.text_area("what you will do")
st.dataframe(df)
st.table(df)
st.plotly_chart(df)
user_name = st.text_input("What is your name?")
if st.button('Submit'):
    st.write(f"Hello {user_name}")

