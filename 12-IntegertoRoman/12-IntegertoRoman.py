            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        roman_string = ""
        for value, roman in char_map:
            roman_string += (num // value) * roman
            num %= value
            (10, 'X'),
            (9, 'IX'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (400, 'CD'),
            (100, 'C'),
            (900, 'CM'),
            (500, 'D'),
    def intToRoman(self, num: int) -> str:
        char_map = [
            (1000, 'M'),
class Solution:
3
