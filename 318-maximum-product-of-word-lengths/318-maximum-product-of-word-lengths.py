class Solution:
    def maxProduct(self, words: List[str]) -> int:
        binary = []
        for i in range(len(words)):
            x = ['0']*26
            c = 0
            for j in words[i]:
                x[ord(j)-97] = '1'
                c += 1
            bin_form = ''.join(x)
            binary.append([int(bin_form,2),c])
        
        max_len = 0
        for j in range(len(binary)):
            for k in range(j+1,len(binary)):
                if binary[j][0] & binary[k][0] == 0:
                    max_len = max(max_len, binary[j][1]*binary[k][1])
        
        return max_len
                    
       
        
        
        