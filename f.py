# Function 1: Sabhi item prices ko jodkar total nikalna (*args use karke)
def calculate_item_total(*prices):
    total = 0
    for p in prices:
        total = total + p
    return total


# Function 2: Discount minus karna aur Tax add karna (Default arguments ke saath)
def apply_discount_and_tax(amount, discount_percent=10, tax_percent=5):
    discount_amount = amount * (discount_percent / 100)
    amount_after_discount = amount - discount_amount

    tax_amount = amount_after_discount * (tax_percent / 100)
    final_amount = amount_after_discount + tax_amount

    return round(final_amount, 2)


# Function 3: Bill receipt print karna
def print_invoice(customer_name, final_bill, payment_mode="Cash"):
    print("\n" + "=" * 35)
    print("        CAFE BILL RECEIPT        ")
    print("=" * 35)
    print(f"Customer Name : {customer_name}")
    print(f"Payment Mode  : {payment_mode}")
    print(f"Total Payable : ₹{final_bill}")
    print("=" * 35)
    print("   Thank you! Visit again :)     ")
    print("=" * 35 + "\n")


# --- Main Program Execution ---

# 1. Items ke prices pass kiye (kitne bhi ho sakte hain)
raw_bill = calculate_item_total(120, 45, 250, 80)
print(f"Items Raw Total: ₹{raw_bill}")

# 2. 10% discount aur 5% tax apply hua (default values)
payable_bill = apply_discount_and_tax(raw_bill)

# 3. Keyword arguments ke sath invoice print kiya
print_invoice(customer_name="Shital", final_bill=payable_bill, payment_mode="UPI")