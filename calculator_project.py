import streamlit as st
import datetime




st.header("CALCULATOR")


option = st.selectbox(
    "Select one operations",
    ('Please Select','Calculator', 'Fixed deposit calculato','Recurring deposit calculator','Loan calculator'))


st.write('You selected:',option)


if option== 'Calculator':
    option = st.radio(
    "Select one operations",
    ('Addition', 'Subtraction','Multiplication','Division'))

    col1, col2 = st.columns(2)
    with col1:
        firstNumber = st.number_input("Enter 1st number")
    with col2:
        secondNumber = st.number_input("Enter 2nd number")

    submit = st.button("Calculate")
    if submit == True:
        if option == 'Addition':
            result = firstNumber + secondNumber
            st.write("Result = ", result)

        elif option == "Subtraction":
            result = firstNumber - secondNumber
            st.write("Result = ", result)

        elif option == "Multiplication":
            result = firstNumber * secondNumber
            st.write("Result = ", result)

        else:
            if secondNumber == 0:
                st.info("second number can be zero at the time of division")
            else:
                result = firstNumber / secondNumber
                st.write("Result = ", result)


elif option == 'Fixed deposit calculato':
    amount = st.slider('Monthly investment ', 5000, 1000000,5000)
    st.write('Principal :',amount)

    rate = st.slider(
        label="Intrest rate ",
        min_value=4.01,
        max_value=20.01,
        step=0.01,
        value=4.50,
        format="%d%%",
    )
    st.write('Intrest rate :',rate)

    tenuer = st.slider('Tenuer', 1, 10, 1)
    st.write('Year :',tenuer)

    maturity=amount+(amount*rate*tenuer/100)
 


    st.write('Invest amount     :',amount)
    st.write('Est. return    :',maturity-amount)
    st.write('Total value    :', maturity)



    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>How can an FD calculator help you ?</h1>", 
            unsafe_allow_html=True)

    st.sidebar.write('Calculating the maturity amount of an FD can be a complicated and time-consuming process. An online FD calculator enables one to figure it without breaking a sweat.')

    st.sidebar.write('1) FD maturity calculations are complex involving multiple variables. A fixed deposit calculator does all the hard work and gives you accurate figures just at the click of a button.')

    st.sidebar.write('2) It helps you save a lot of time on these complex calculations')

    st.sidebar.write('3) A fixed deposit return calculator enables you to compare the maturity amount and interest rates of FDs offered by different financial institutions. You can make an informed decision when you have all the figures at your disposal')

    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>The formula to determine FD maturity amount</h1>", 
            unsafe_allow_html=True)

    st.sidebar.write('There are two types of FD that you may avail of – simple interest FD and compound interest FD. This calculators for both types of FD.')

    st.sidebar.write('The fixed deposit calculator for simple interest FD uses the following formula –')

    st.sidebar.write('M = P + (P x r x t/100), where –')

    st.sidebar.write('1) P is the principal amount that you deposit')

    st.sidebar.write('2) r is the rate of interest per annum')

    st.sidebar.write('3) t is the tenure in years')

    
elif option == 'Recurring deposit calculator':
    principal = st.number_input("Enter the amount")
    time = st.number_input("Enter the number of periods (months):", min_value=1, step=1)

    interest_rate = st.number_input("Enter the interest rate per period (%):", min_value=0.0, max_value=100.0, step=0.1)

    submit = st.button("Calculate")
    if submit == True:
    
        interest= principal * time * (time+1) * interest_rate / 2400
        rd = principal * time + interest

        total_savings = principal*time
        total_interest = rd- total_savings
        
        st.write('Maturity Amount   :',rd)
        st.write('Total Interest Earned  :',total_interest)
        
    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>How to Use RD Calculator ?</h1>", 
            unsafe_allow_html=True)

    st.sidebar.write('RD Calculator is used to determine the amount of money you will receive once your RD matures. You can use the RD Calculator offered by several banks or a simple formula to determine the amount. Using the RD Calculator can help you get the results immediately and the process is hassle-free. The interest that is generated from an RD account is compounded quarterly.')
    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Advantages of Using the RD Calculator</h1>", 
            unsafe_allow_html=True)
    
    st.sidebar.write('Some of the main advantages of using the RD Calculator are mentioned below:')
    st.sidebar.write('1) Accurate estimations are provided.')
    st.sidebar.write('2) Saves time and is convenient')
    st.sidebar.write('3) You can plan your finances in the long run.')

    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>How to Calculate the RD interest Rate ?</h1>", 
            unsafe_allow_html=True)
    st.sidebar.write('The interest amount on recurring deposits is usually compounded on a quarterly basis:')
    st.sidebar.write('The following formula is used by banks to calculate how much the interest component on a recurring deposit will be at maturity:')
    st.sidebar.write('M =R[(1+i) n - 1]/1-(1+i) (-1/3)')
    st.sidebar.write('Note:')
    st.sidebar.write('M = Maturity value of the RD')
    st.sidebar.write('R = Monthly installment credited in the RD')
    st.sidebar.write('n = Number of quarters (in the total tenure)')
    st.sidebar.write('i = Rate of Interest / 400')


elif option== 'Loan calculator':
    loan_amount = st.number_input("Enter the amount")
    loan_years = st.number_input("Enter the number of periods (Years):", min_value=1, step=1)

    interest_rate = st.number_input("Enter the interest rate per period (%):", min_value=0.0, max_value=100.0, step=0.1)
    
    submit=st.button("Calculate")
    if submit== True:
        
        monthly_rate = interest_rate / 1200

        num_payments = loan_years * 12
        try:
            emi = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** (-num_payments))
            total_interest = emi * num_payments - loan_amount
            total_payment = emi * num_payments
            st.subheader("Loan Summary")
            st.write("Loan Amount: ",loan_amount)
            st.write("Monthly Payment (EMI): ", round(emi, 2))
            st.write("Total Intrest :",round(total_interest))
            st.write("Total Payment :",round(total_payment))
        except ZeroDivisionError:
            st.error("Error: Cannot divide by zero")

     

    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>What is EMI ?</h1>", 
            unsafe_allow_html=True)
    st.sidebar.write('''Equated Monthly Installment - EMI for short - is the amount payable every month to the bank or any other financial institution until the loan amount is fully paid off. It consists of the interest on loan as well as part of the principal amount to be repaid. The sum of principal amount and interest is divided by the tenure, i.e., number of months, in which the loan has to be repaid. This amount has to be paid monthly. The interest component of the EMI would be larger during the initial months and gradually reduce with each payment. The exact percentage allocated towards payment of the principal depends on the interest rate. Even though your monthly EMI payment won't change, the proportion of principal and interest components will change with time. With each successive payment, you'll pay more towards the principal and less in interest.''')

    st.sidebar.write('''Here's the formula to calculate EMI:''')
    st.sidebar.write('EMI = [P x r x (1+r)^n]/[(1+r)^n-1]')
    st.sidebar.write('Where,')
    st.sidebar.write('P = Principal amount (loan amount)')
    st.sidebar.write('r = Rate of interest per month  \n(i.e., Annual interest rate divided by 12)')
    st.sidebar.write('n = Number of monthly installments')

    st.sidebar.write('''The formula assumes that the interest is compounded monthly and the repayment is made in equated monthly installments over the loan tenure. By using this formula, one can easily calculate the monthly installment to be paid for a loan, which helps in managing finances and planning monthly budgets accordingly.''')


else:
    st.write('')


