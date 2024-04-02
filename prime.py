# check if it is a prime number
def is_prime(num):
    not_prime = False
    for i in range(2, num):
        if num % i == 0 and i != num:  # check if it is not prime
            not_prime = True  # return True if it is not prime
    return not_prime


input_num = int(input("Type a number: "))

if is_prime(input_num):
    print("Isn't prime")  # in case its True
else:
    print("Is prime")  # in case its False
