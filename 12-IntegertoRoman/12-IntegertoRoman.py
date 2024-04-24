            (400, 'CD'),
            (100, 'C'),
            (50, 'L'),
            (10, 'X'),
            (5, 'V'),
            (1, 'I')
        ]
            (90, 'XC'),
            (40, 'XL'),
            (9, 'IX'),
            (4, 'IV'),

        for value, roman in char_map:
        roman_string = ""
            roman_string += (num // value) * roman
            num %= value

        return roman_string 





3
