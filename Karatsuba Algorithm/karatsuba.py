# KARATSUBA MULTIPLICATION ALGORITHM(BASE 10)

def main():
    # Multiplying two large numbers.
    karatsuba(1542256564751236452, 4523215642154352)
    karatsuba(-2536415853, 215341562)
    karatsuba(154225656475122536452, 45232152514642154352)

def karatsuba(a, b):
    a1 = abs(a)
    b1 = abs(b)
    result = multiply(str(a1),str(b1))
    # for negative numbers.
    if a < 0 or b < 0:
        if a < 0 and b < 0:     
            print(result)
        else:
            # Add a negative sign to the result.
            print('-', end='')    
            print(result)
    else:
        print(result)        

# Recursive function for karatsuba multiplication.
def multiply(str1, str2):
    p = len(str1)
    q = len(str2)
    # Number of digits.(you can assign p or q, -will update later)
    n = p
    # Multiply and return the value if the number of digits is <= 5.
    if p <= 5 and q <= 5:
        return int(str1) * int(str2)

    # Pad zeros to the shorter string.(to make the strings of equal length)
    if p > q:
        # Pad zeros
        str2 = str2.zfill(p)
        # update n
        n = p
    if q > p:
        # Pad zeros
        str1 = str1.zfill(q)
        # update n
        n = q

    i = int(n / 2)
    m = n - i
    # first half of the characters of str1 from left and right respectively.
    high1 = str1[0 : i]
    low1 = str1[i : n]
    
    # first half of the characters of str2 from left and right respectively.
    high2 = str2[0 : i]
    low2 = str2[i : n]

    # recursive call for multiplying the numbers.
    z0 = multiply(high1, high2)
    z1 = multiply(low1, low2)
    
    # arithmetic to obtain the z2 by single multiplication
    # and few extra additions.
    x1 = int(high1) + int(low1)
    x2 = int(high2) + int(low2)
    x3 = multiply(str(x1), str(x2))
    
    z2 = x3 - z0 - z1
    
    # Convert to strings for padding the appropriate number of 
    # trailing zeros befor addition.
    k0 = str(z0)
    k2 = str(z2)
 
    # padding zeros and adding to get the final result.
    k0 = int(k0.ljust(2*m + len(k0), '0'))
    k2 = int(k2.ljust(m + len(k2), '0'))

    return (k0 + k2 + z1)

# Call the main function to execute the code.
main()
