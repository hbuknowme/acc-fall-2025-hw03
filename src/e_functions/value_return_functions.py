FICA_RATE = 0.0765
FEDERAL_RATE = 0.08

def get_gross_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        gross = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross = hours * rate
    return gross

def get_fica_tax(gross):
    return gross * FICA_RATE

def get_federal_tax(gross):
    return gross * FEDERAL_RATE
