# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

import math

def iterations(n: int, record: dict={1: 1}) -> int:
    if n in record:
        return record[n]
    if n % 2 == 0:
        return 1 + iterations(n // 2, record)
    return 1 + iterations(3 * n + 1, record)

counts = {2**x: x + 1 for x in range(1, int(math.log(10**6, 2)))}
biggest = 1

for i in range(1,10**6):
    if i not in counts:
        counts[i] = iterations(i, counts)
    biggest = i if counts[i] > counts[biggest] else biggest


stream = open("results.txt", 'w')
stream.write("\nBiggest: %d" %biggest)
stream.close()
stream = open("results.txt")
print(stream.read())
stream.close()