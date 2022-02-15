class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_list = [
            ["M",1000],
            ["CM",900],
            ["D",500],
            ["CD",400],
            ["C",100],
            ["XC",90],
            ["L",50],
            ["XL",40],
            ["X",10],
            ["IX",9],
            ["V",5],
            ["IV",4],
            ["I",1]
        ]
        
        roman_string = ""
        
        for sym,val in symbol_list:
            # we always choose the largest value and see if its part of the roman string or not
            if num // val != 0:
                contribution = num // val
                roman_string += sym*contribution
                # reduce the value after using up the largest roman value
                num = num % val
        
        return roman_string
                
        