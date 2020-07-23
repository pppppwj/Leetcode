class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        
        digit_to_letters = {
            2:{"a","b","c"},3:{"d","e","f"},4:{"g","h","i"},
            5:{"j","k","l"},6:{"m","n","o"},7:{"p","q","r","s"},
            8:{"t","u","v"},9:{"w","x","y","z"}
        }
        

        def aux(output,digits):
            if not digits:
                return output
            else:
                n = int(digits[0])
                return aux([old+new for old in output for new in digit_to_letters[n]],digits[1:])

        return aux([""],digits)