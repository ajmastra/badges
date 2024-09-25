import streamlit as st

# header container
with st.container():
    
    # title and sub header
    st.title("🧮 Calculator")
    st.write("A basic arithmetic calculator for simple computation.")
    
# calculator container
with st.container():
    st.write("---")

    # input 1
    number1 = st.number_input(label="Enter the first number")

    # input 2
    number2 = st.number_input(label="Enter the second number")

    st.write("Operation")

    # create the radio for operands
    operation = st.radio("Select an operation to perform on the given numbers:",
                                    ("Add", "Subtract", "Multiply", "Divide",
                                                                    "Modulus"))

    # intialize the answer to 0
    answer = 0.0

    # initialize calculate function
    def calculate():

        # if user selected add
        if operation == "Add":
            answer = number1 + number2
        # else if user selected subtract
        elif operation == "Subtract":
            answer = number1 - number2
        # else if user selected multiply
        elif operation == "Multiply":
            answer = number1 * number2
        # else if user selected divide
        elif operation == "Divide" and number2 != 0:
            answer = number1 / number2
        # else if user selected modulus
        elif operation == "Modulus":
            answer = number1 % number2
        # otherwise there is a division by 0 error
        else:
            st.warning("Division by 0 error. Please enter a non-zero number.")
            answer = "Not defined"

        st.success(f"Answer = {answer}")

    if st.button("Calculate"):
        calculate()
