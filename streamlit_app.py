
import streamlit as st

# Set up the title and description
st.title("BMI Calculator Dashboard")
st.write("Calculate your Body Mass Index (BMI) using your height and weight.")

# Input for weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)

# Input for height in meters
height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01)

# Calculate BMI
if weight and height:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Provide BMI interpretation
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.write("Please enter both weight and height to calculate BMI.")

# Footer
st.write("---")
st.write("Developed with Streamlit. BMI = weight(kg) / height(m)^2")
