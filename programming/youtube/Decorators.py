def ticket_price(age: int):
    if age < 16:
        print("$20")
    else:
        print("$30")


def verify_age(func):
    def verifier(age):
        if age < 13:
            print("Sorry, you're not allowed for this show")
            return
        return func(age)
    return verifier


ticket_price = verify_age(ticket_price)
ticket_price(27)
