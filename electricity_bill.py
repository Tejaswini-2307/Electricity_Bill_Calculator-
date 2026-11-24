
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


# NEW CODE: Discount Calculation
def discount(bill):
    if bill >= 1000:
        return bill * 0.10
    else:
        return 0


# Main Program
print("===== Electricity Bill Calculator =====")

units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units!")
else:
    cost = units_cost(units)
    fixed = fixed_charge()
    bill = total_bill(units)

    # NEW CODE: Apply Discount
    discount_amount = discount(bill)
    final_bill = bill - discount_amount

    print("\n----- Electricity Bill -----")
    print("Units Consumed:", units)
    print("Units Cost: Rs.", cost)
    print("Fixed Charge: Rs.", fixed)
    print("Total Bill: Rs.", bill)
    print("Discount: Rs.", discount_amount)
    print("Final Bill: Rs.", final_bill)
