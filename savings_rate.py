def get_monthly_savings_rate():
    # Get user input
    gross_annual_income = float(input("Enter your gross annual income: "))
    monthly_savings = float(input("Enter your total monthly savings (including 401k, IRA, savings accounts, etc.): "))
    monthly_net_income = float(input("Enter your monthly net income: "))

    # Calculate gross monthly income
    gross_monthly_income = gross_annual_income / 12

    # Calculate difference between gross and net income
    income_diff = gross_monthly_income - monthly_net_income
    net_income_percentage = (monthly_net_income / gross_monthly_income) * 100

    # Calculate savings rate
    savings_rate_gross = (monthly_savings / gross_monthly_income) * 100
    savings_rate_net = (monthly_savings / monthly_net_income) * 100

    return savings_rate_gross, savings_rate_net, income_diff, net_income_percentage


# Run the function and print the savings rates
savings_rate_gross, savings_rate_net, income_diff, net_income_percentage = get_monthly_savings_rate()
print('\n')
print(f"Your monthly savings rate based on gross income is {savings_rate_gross:.2f}%")
print(f"Your monthly savings rate based on net income is {savings_rate_net:.2f}%")
print(f"The monthly difference between your gross and net income is ${income_diff:.2f}")
print(f"Your net income is {net_income_percentage:.2f}% of your gross income.")
