import streamlit as st
import pandas as pd
import joblib


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")
Location_opt = joblib.load("Location.pkl")
Brand_opt = joblib.load("Brand.pkl")
Fuel_Type_opt = joblib.load("Fuel_Type.pkl")
Transmission_opt = joblib.load("Transmission.pkl")
def prediction(Location, Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Mileage, Engine, Power, Seats, Brand):
    test_df = pd.DataFrame(columns= Inputs)
    test_df.at[0,"Location"] = Location
    test_df.at[0,"Year"] = Year
    test_df.at[0,"Kilometers_Driven"] = Kilometers_Driven
    test_df.at[0,"Fuel_Type"] = Fuel_Type
    test_df.at[0,"Transmission"] = Transmission
    test_df.at[0,"Owner_Type"] = Owner_Type
    test_df.at[0,"Mileage"] = Mileage
    test_df.at[0,"Engine"] = Engine
    test_df.at[0,"Power"] = Power
    test_df.at[0,"Seats"] = Seats
    test_df.at[0,"Brand"] = Brand
    result = Model.predict(test_df)[0]
    return result

def main():
    st.title("Used Cars Price")
    Location = st.selectbox("Location" , list(Location_opt))
    Brand = st.selectbox("Brand" , list(Brand_opt))
    Fuel_Type = st.selectbox("Fuel_Type" , list(Fuel_Type_opt))
    Transmission = st.selectbox("Transmission" , list(Transmission_opt))
    Kilometers_Driven = st.slider("Kilometers_Driven" , min_value= 0 , max_value=500000 , value=0,step=1000) 
    Owner_Type = st.slider("Owner_Type" , min_value= 1 , max_value=5 , value=1,step=1)   
    Mileage = st.slider("Mileage" , min_value= 4 , max_value=16 , value=4,step=1) 
    Engine = st.slider("Engine" , min_value= 600 , max_value=6000 , value=600,step=100) 
    Power = st.slider("Power" , min_value= 30 , max_value=560 , value=30,step=10)
    Seats = st.slider("Seats" , min_value= 2 , max_value=10 , value=2,step=1)
    Year = st.slider("Year" , min_value= 1998 , max_value=2020 , value=1998,step=1)  

    if st.button("predict"):
        result = prediction(Location, Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Mileage, Engine, Power, Seats, Brand)
        st.text(f"The Price will be {result}")

if __name__ == '__main__':
    main()
