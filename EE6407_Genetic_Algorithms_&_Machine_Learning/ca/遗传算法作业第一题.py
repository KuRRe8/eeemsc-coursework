import numpy as np
import math

# ackley函数
def Ackley(x:list, n:int = 4) -> float:

    assert len(x) == n
    a = 20; b = 0.2; c = 2*np.pi
    sum1 = 0
    sum2 = 0
    for i in range(0,n):
       sum1 = sum1+x[i]**2
       sum2 = sum2+math.cos(c*x[i])
    
    yPart1 = -a*math.exp(-b*math.sqrt(1/n*sum1))
    yPart2 = -math.exp(1/n*sum2)
    yPart3 = a+math.exp(1)
    y = yPart1+yPart2+yPart3
    #truncation found beneath, not to be used
    #y = -a*math.exp(-b*math.sqrt(1/n*sum1))-math.exp(1/n*sum2)+a+math.exp(1)
    return y

def gamma(bins:list, L:int = 4) -> float:

    assert len(bins) == L
    x = -2
    y = 2
    sum1 = 0
    for j in range(0,L):
        sum1 = sum1+bins[L-1-j]*2**j
    
    result = x+(y-x)/((2**L)-1)*sum1

    return result

if __name__ == "__main__":
    bi_string_a = [[1,0,1,1],[1,1,0,0],[1,0,1,1],[0,0,1,0]]
    bi_string_b = [[0,0,1,1],[1,1,0,0],[1,0,1,1],[0,0,1,0]]
    bi_string_c = [[1,1,1,1],[1,1,0,1],[1,0,0,1],[0,0,1,1]]
    bi_string_d = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
    print("Ackely(a) = ",end = "")
    print(Ackley([gamma(bi_string_a[0]),gamma(bi_string_a[1]),gamma(bi_string_a[2]),gamma(bi_string_a[3])],4))
    print("Ackely(b) = ",end = "")
    print(Ackley([gamma(bi_string_b[0]),gamma(bi_string_b[1]),gamma(bi_string_b[2]),gamma(bi_string_b[3])],4))
    print("Ackely(c) = ",end = "")
    print(Ackley([gamma(bi_string_c[0]),gamma(bi_string_c[1]),gamma(bi_string_c[2]),gamma(bi_string_c[3])],4))
    print("Ackely(d) = ",end = "")
    print(Ackley([gamma(bi_string_d[0]),gamma(bi_string_d[1]),gamma(bi_string_d[2]),gamma(bi_string_d[3])],4))