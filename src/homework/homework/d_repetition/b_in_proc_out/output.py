# constant tax rate
TAX_RATE = 0.0675

def get_sales_tax_amount(meal_amount):
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount, tip_rate):
    return meal_amount * tip_rate
