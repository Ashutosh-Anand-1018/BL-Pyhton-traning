def emi_calculator(P: float, R: float, Y: float):
    rate = R / (12 * 100)
    n = Y * 12
    monthly_payment = (P * rate * (1 + rate) ** n) / ((1 + rate) ** n - 1)
    return monthly_payment

principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate: "))
years = float(input("Enter the number of years: "))

monthly_emi = emi_calculator(principal, annual_rate, years)
print(f"The monthly car loan payment: {monthly_emi:.2f}")