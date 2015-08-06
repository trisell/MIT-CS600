

balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
payment = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
print "Month: 1"
minimum_monthly_payment = payment * balance
print "Minimum monthly payment: $%.2f" % minimum_monthly_payment
interest_paid = (interest / 12) * balance
principal_paid = minimum_monthly_payment - interest_paid
print "Principal paid: $%.2f" % principal_paid
remaining_balance = balance - principal_paid
print "$%d" % remaining_balance

for i in xrange(2, 13):
    print "Month: %s" % i
    minimum_monthly_payment = payment * remaining_balance
    print "Minimum monthly payment: $%.2f" % minimum_monthly_payment
    interest_paid = (interest / 12) *remaining_balance
    principal_paid = minimum_monthly_payment - interest_paid
    print "Principal paid: $%.2f" % principal_paid
    remaining_balance = remaining_balance - principal_paid
    print "$%.2f" % remaining_balance
    i += 1
   


