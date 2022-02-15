class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #base cases
        if n < 1:
            return 0
        if n == 1:
            return 1
        
        # main algorithm to get nth ugly number
        ugly_numbers = [1]*n
        pointer_2 = 0
        pointer_3 = 0
        pointer_5 = 0
        for i in range(1,n):
            ugly_numbers[i] = min(ugly_numbers[pointer_2]*2, ugly_numbers[pointer_3]*3, ugly_numbers[pointer_5]*5)
            if ugly_numbers[i] == ugly_numbers[pointer_2]*2:
                pointer_2 += 1
            if ugly_numbers[i] == ugly_numbers[pointer_3]*3:
                pointer_3 += 1
            if ugly_numbers[i] == ugly_numbers[pointer_5]*5:
                pointer_5 += 1
        return ugly_numbers[n-1]