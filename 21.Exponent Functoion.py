#this is 2 raised of the power 3
print(2**3)
print("-------------------")
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,2))