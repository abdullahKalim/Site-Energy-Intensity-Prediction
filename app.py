#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[5]:


st.set_page_config(page_title='Site Energy Prediction',layout='wide')
st.markdown("<h1 style='text-align: center;'>Site Energy Prediction App </h1>", unsafe_allow_html=True)


# In[6]:


from PIL import Image
image=Image.open("C:\\Users\\hp\\Documents\\site_energy_prediction.jpg")
st.image(image)


# In[7]:


state_factor=["State_1","State_2","State_3","State_4","State_5","State_6"]


# In[11]:


def main():
    with st.form('prediction form'):
        st.subheader("Enter the following features")
        year_f=st.slider("Year Factor: ",1,6,value=1,format="%d")
        state_f=st.selectbox("State Factor: ",options=state_factor)
        build_class=st.radio("Building class: ",options=["Residential","Commercial"])
        floor=st.number_input("Floor Area: ",0)
        year=st.number_input("Year Built: ",1600)
        star=st.slider("Energy Star Rating: ",1,100)
        submit=st.form_submit_button("Predict")
        if submit:
            st.write("Prediction is ")


# In[12]:


if __name__ == '__main__':
    main()


# In[ ]:




