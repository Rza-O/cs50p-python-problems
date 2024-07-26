def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.replace("$", "")) #here I turned strin d to a float d and replaced $
    return d

def percent_to_float(p):
    p = float(p.replace("%", "")) #here I turned strin p to a float p and replaced %
    p = p/100                     # here i calculated the percentages
    return p
main()
