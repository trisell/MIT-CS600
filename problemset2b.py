

balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
monthly_lowest = balance / 12.0
monthly_interest = interest / 12.0
monthly_upper = (balance * (1 + monthly_interest) ** 12.0) / 12.0
lowest_balance = 0.01

while balance > lowest_balance:

	payment = (monthly_upper - monthly_lowest) / 2 + monthly_lowest

	for month in xrange(12):
		balance -= payment
		balance *= monthly_interest

		if balance > 0:
			monthly_lowest = payment

		else:
			monthly_upper = payment

	print "Monthly Payment to pay off debt in 1 year: %.2f" % payment
	print "Number of months needed: " month
	print "Balance: %.2f" % balance 