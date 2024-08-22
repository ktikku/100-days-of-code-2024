def calcualte_binary(num):
    res = []
    while num >= 1:
        res.append(num % 2)
        num = num // 2
    return res

def calculate_dec(res):
    number = 0
    for i in range(len(res)):
        if res[i] == 1:
            multiplier = 0
        else:
            multiplier = 1
        number += multiplier * pow(2, i)
    return number

class Solution:
    def findComplement(self, num: int) -> int:
        binary = calcualte_binary(num)
        return calculate_dec(binary)