# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_payments = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.
       # 12345678901234567890123456789012345678901234567890
print("Payment Number Total Paid    Principal")
while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    if num_payments >= extra_payment_start_month and num_payments <= extra_payment_end_month:
        total_paid = total_paid + extra_payment
        principal = principal - extra_payment
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    num_payments = num_payments + 1
    print(f"{num_payments:<14} {round(total_paid, 2):<13} {round(principal, 2)}")
if principal < 0:
    total_paid = total_paid + principal
principal = 0

print(f'Total paid, {total_paid:.2f}')
print(f'Number of Monthly Payments, { num_payments}')
