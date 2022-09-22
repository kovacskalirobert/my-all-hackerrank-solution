#  input:   string (S)
#           integer (k)
#  --------------------
#  output:  Print the different combinations of string S on separate lines.
#  

from itertools import combinations


S, k = input().split()
k = int(k)
S = sorted(list(S))

for i in range(1, k+1):
    comb = list(combinations(S, i))
    for value in comb:
        print(''.join(value))

