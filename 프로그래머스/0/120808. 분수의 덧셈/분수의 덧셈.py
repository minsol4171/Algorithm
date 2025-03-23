def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    top = numer1 * denom2 + numer2 * denom1
    bottom = denom1 * denom2
    
    common = gcd(top, bottom)
    return [top//common, bottom//common]