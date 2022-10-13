"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    length = 0
    index = 1
    if number_of_primes <= 0:
        raise ValueError("Input number is invalid")
    while length < number_of_primes:
        count = 0
        for j in range(1,index + 1):
            if index%j == 0:
                count +=1
        if count == 2:
            list.append(index)
            length +=1
        index +=1
            
    
    return list

