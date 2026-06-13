class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        L=[]
        for d in digits:
            L.append(int(d))
    # Creating Dictionary So that we can access values through keys!!!!!
        L1={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[""]
        for digit in L:
            letters=L1[digit]
            new_rs=[]
            for c in res:
                for l in letters:
                    new_rs.append(c + l)
            res=new_rs
        return res
        