from output import get_sales_tax_amount, get_tip_amount

def main():
    meal_amount = float(input("Enter the meal amount: "))
    tip_rate = float(input("Enter the tip rate as a decimal (example 0.15): "))

    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount

    print("\nReceipt")
    print(f"Meal Amount: {meal_amount}")
    print(f"Sales Tax: {sales_tax}")
    print(f"Tip Amount: {tip_amount}")
    print(f"Total: {total}")

main()
