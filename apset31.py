a=int(input())
d=int(input())
n=int(input())
def  sumOfAP(a,  d,  n):
    sum = (n / 2) * (2 * a + (n - 1) * d)
    return sum
 
print(sumOfAP(a, d, n))
