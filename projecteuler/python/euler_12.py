def list_sum(nums: list) -> int:
    total = 0    
    for num in nums:
        total += num
    return total

def list_mean(nums: list) -> float:
    return list_sum(nums) / len(nums)

def count_factors(n: int) -> int:
    facts = 0
    for test in range(2, int(n ** 0.5) + 1):
        if n % test == 0:
            facts += 2
    if (n ** 0.5) * (n ** 0.5) == n:
        facts -= 1
    return facts

def make_tri_num(num: int) -> int:
    tri = 0
    for i in range(1,num + 1):
        tri += i
    return tri

def n_divisors(n: int) -> int:
    test, divs, last_five = n // 2, 0, []
    while divs < n:
        tri = make_tri_num(test)
        divs = count_factors(tri)
        test += 1
        print("%dth triangle num: %d \nDivisors: %d" %(test, tri, divs))
    
    return tri

if __name__ == "__main__":
    print(n_divisors(500))