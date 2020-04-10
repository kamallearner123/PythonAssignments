'''
Write a function to find the given number is prime or not.


def isprime(num):
    pass

print(isprime(10001))

'''
def isprime(num):
    '''
    Going to maintain a flag: Flag will be set 0 is it is not prime.
    '''
    flag = 1
    for i in range(2, num//2):# integer division is required
        if num%i == 0:
            print("Can be devided it by %d"%(i))
            flag = 0
            break
    if flag == 1:
        return True
    else:
        return False
    
print(isprime(21))
