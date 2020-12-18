def interest(n, principle_amount):
    def years(x):
        return principle_amount + (n * principle_amount * x) / 100

    return years


principle = 100000
home_loan = interest(7, principle)  # percentage of 7
personal_loan = interest(11, principle)  # percentage of 11

print(home_loan(20))  # for 20 years
print(personal_loan(3))  # for 3 years
