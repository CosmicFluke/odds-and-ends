import math

def pythagorean_triplet(n: int) -> (int, int, int):
    cap1 = n - 2
    for a in range(1, cap1):
        cap2 = n - a - 1
        for b in range(1, cap2):
            c = math.sqrt(a ** 2 + b ** 2)
            if int(c) == c and a + b + c == n:
                return a, b, int(c)
    print("No such triplet")    
    return None, None, None

a, b, c = pythagorean_triplet(1000)
print("%d x %d x %d = %d" %(a, b, c, a * b * c))