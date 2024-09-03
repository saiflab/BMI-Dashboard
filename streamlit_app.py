import streamlit as st

# Set up the title and logo
st.image("logo.jpg", use_column_width=True)
st.title("BMI Calculator Dashboard")
st.write("Calculate your Body Mass Index (BMI) using your height and weight.")

# Input for weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)

# Input for height in inches
height_in = st.number_input("Enter your height (inches):", min_value=1.0, step=0.1)

# Convert height to meters for BMI calculation
height_m = height_in * 0.0254

# Calculate BMI
if weight and height_in:
    bmi = weight / (height_m ** 2)
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
st.markdown("**Created by Ahmed Saif**", unsafe_allow_html=True)
