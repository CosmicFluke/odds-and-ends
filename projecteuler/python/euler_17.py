nums = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'}

def count_letters(n, b=1):
    if n == b - 1:
        return 0
    a = n
    digs = [0,0,0,0]
    for dig in range(4):
        digs[dig] = a % 10
        a = a // 10
    letters = 0
    if (digs[0] + digs[1] * 10) <= 20:
        letters += len(nums[digs[0] + digs[1] * 10])
    else:
        letters += len(nums[digs[0]]) + len(nums[digs[1] * 10])
        
    if digs[2] > 0:
        letters += len(nums[digs[2]]) + len(nums[100])
        if digs[1] + digs[0] > 0:
            letters += 3
    if digs[3] > 0:
        letters += len(nums[digs[3]]) + len(nums[1000])
    return letters + count_letters(n - 1, b)

count = 0
for i in range(10, 1001, 10):
    num = count_letters(i, i-9)
    print(num)
    count += num
print(count)
