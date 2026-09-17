class Solution:
    def isHappy(self, n: int) -> bool:
        nu = str(n)
        num = []
        for c in nu:
            num.append(c)
        # print(num)
        seen = set()
        while True:
            sum = 0
            for i in num:
                sum += int(i) **2
            if sum in seen:
                return False
            if sum ==1:
                return True
            seen.add(sum)
            nu = str(sum)
            num =[]
            for c in nu:
                num.append(c)
        return False

        