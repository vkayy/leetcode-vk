class Solution:
    def intToRoman(self, num: int) -> str:
        
        itr = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50:  "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        
        res = ""
        for i, r in itr.items():
            while num >= i:
                num -= i
                res += r
        return res

# we create a dictionary called itr, mapping integers to roman numerals
# we create a variable called res and set it to ""
# we iterate through the items in itr
# for each item, we iterate while num is greater than or equal to the integer
# we subtract the integer from num and add the roman numeral to res
# return res