# This is the streamlit code for building user interface and printing output on the screen
# You will need to open any of the python editor like Pycharm or sypder and paste this code and then in the terminal of the editor run the command - "streamlit run file_name"
# this will host your webapp on your device 

import numpy as np
import pickle as pkl
import streamlit as st
filepath = "C:\\Users\\lenovo\\sdp107\\iris_model.sav"  # here you will need to paste the file path of your jupyter notebook file(code)
load_model = pkl.load(open(filepath, "br"))
def pred(x):
 x = np.asarray(x).reshape(1,-1)
 result = load_model.predict(x)
 if result[0] == 0:
    return("Satosa")
 elif(result[0] == 1):
    return("Versicolor")
 else:
    return("verginica")
def main():
 sl = st.number_input("Sepal-length")
 sw = st.number_input("Sepal-width")
 pl = st.number_input("Petal-length")
 pw = st.number_input("Petal-width")

 data = [sl, sw, pl, pw]

 if st.button("Predict"):
    st.write(pred(data))

if __name__ == "__main__":
 main()
