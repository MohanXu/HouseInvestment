import numpy as np
import matplotlib.pyplot as plt


def calculate_rent(price, interest_rate=0.0647, loan_term_years=30, property_tax=418, insurance=102, hoa=38,
                   target_return_rate=0.1):
    # Constants
    down_payment = 0.2 * price
    loan_amount = 0.8 * price
    monthly_interest_rate = interest_rate / 12
    total_months = loan_term_years * 12

    # Monthly mortgage payment calculation
    M = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -total_months)

    # Total monthly expenses
    total_monthly_expenses = M + property_tax + insurance + hoa

    # Target monthly profit
    target_annual_profit = 0.02 * price
    target_monthly_profit = target_annual_profit / 12

    # Rent calculation
    # R - (total_monthly_expenses + (R / 12) + 0.1R) = target_monthly_profit
    # R - 0.1R - (R / 12) = target_monthly_profit + total_monthly_expenses
    # 0.9R - (R / 12) = target_monthly_profit + total_monthly_expenses
    # (0.9 - 1/12)R = target_monthly_profit + total_monthly_expenses
    # R = (target_monthly_profit + total_monthly_expenses) / (0.9 - 1/12)

    rent = (target_monthly_profit + total_monthly_expenses) / (0.9 - 1 / 12)
    return rent


def plot_rent_vs_price(prices, interest_rate=0.0647, loan_term_years=30, property_tax=418, insurance=102, hoa=38,
                       target_return_rate=0.1):
    rents = [calculate_rent(price, interest_rate, loan_term_years, property_tax, insurance, hoa, target_return_rate) for
             price in prices]

    plt.figure(figsize=(10, 6))
    plt.plot(prices, rents, marker='o')
    plt.title('Required Rent vs. House Price')
    plt.xlabel('House Price ($)')
    plt.ylabel('Required Monthly Rent ($)')
    plt.grid(True)
    plt.show()


# Example usage
prices = np.linspace(100000, 400000, 10)  # Example range of house prices from $100,000 to $1,000,000
plot_rent_vs_price(prices)