
# Electricity Bill Calculator

def units_cost(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + (units - 100) * 5
    else:
        return (100 * 3) + (100 * 5) + (units - 200) * 7


def fixed_charge():
    return 50


def total_bill(units):
    return units_cost(units) + fixed_charge()


# Main program
print("===== Electricity Bill Calculator =====")

units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units!")
else:
    print("Units Consumed:", units)
    print("Units Cost: Rs.", units_cost(units))
    print("Fixed Charge: Rs.", fixed_charge())
    print("Total Electricity Bill: Rs.", total_bill(units))
