def exponent(base, power):
    result = 1
    for index in range (power):
        result = result * base
    return result

base = input("Enter a base: ")
power = input("Enter the power: ")

print(exponent(int(base),int(power)))