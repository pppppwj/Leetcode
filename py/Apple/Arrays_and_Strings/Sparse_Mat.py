

class SparseMatrix():

    def __init__(self,values,cols,rows):
        # also can set *args 
        # len(args) == 1 or 3
        self.V=values
        self.COL_INDEX=cols
        self.ROW_INDEX=rows

    @classmethod
    def array2sp(cls,nums):
        V=[]
        COL_INDEX=[]
        ROW_INDEX=[]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if nums[i][j]:
                    V.append(nums[i][j])
                    COL_INDEX.append(j)
                    ROW_INDEX.append(i)
        return cls(V,COL_INDEX,ROW_INDEX)
    
    def display(self):
        print("V = ",self.V)
        print("COL_INDEX = ",self.COL_INDEX)
        print("ROW_INDEX = ",self.ROW_INDEX)

    def __add__(self,other):
        V=[]
        COL_INDEX=[]
        ROW_INDEX=[]
        # i for self, j for other
        i=j=0
        while (i<len(self.V) and j<len(other.V)):
            # case 1 row1 != row2
            if self.ROW_INDEX[i] < other.ROW_INDEX[j]:
                V.append(self.V[i])
                COL_INDEX.append(self.COL_INDEX[i])
                ROW_INDEX.append(self.ROW_INDEX[i])
                i+=1
            elif self.ROW_INDEX[i] > other.ROW_INDEX[j]:
                V.append(other.V[j])
                COL_INDEX.append(other.COL_INDEX[j])
                ROW_INDEX.append(other.ROW_INDEX[j])
                j+=1
            elif self.ROW_INDEX[i] == other.ROW_INDEX[j]:
                # case 2 col1 != col2
                if self.COL_INDEX[i] < other.COL_INDEX[j]:
                    V.append(self.V[i])
                    COL_INDEX.append(self.COL_INDEX[i])
                    ROW_INDEX.append(self.ROW_INDEX[i])
                    i+=1
                
                elif self.COL_INDEX[i] > other.COL_INDEX[j]:
                    V.append(other.V[j])
                    COL_INDEX.append(other.COL_INDEX[j])
                    ROW_INDEX.append(other.ROW_INDEX[j])
                    j+=1
                
                else:
                    V.append(self.V[i]+other.V[j])
                    COL_INDEX.append(self.COL_INDEX[i]+other.COL_INDEX[j])
                    ROW_INDEX.append(self.COL_INDEX[i]+other.COL_INDEX[j])
                    i+=1
                    j+=1

        while(i<len(self.V)):
            V.append(self.V[i])
            COL_INDEX.append(self.COL_INDEX[i])
            ROW_INDEX.append(self.ROW_INDEX[i])
            i+=1
        
        while(j<len(other.V)):
            V.append(self.V[j])
            COL_INDEX.append(other.COL_INDEX[j])
            ROW_INDEX.append(other.ROW_INDEX[j])
            j+=1

        return SparseMatrix(V,COL_INDEX,ROW_INDEX)

    def transpose(self):
        return SparseMatrix(self.V,self.ROW_INDEX, self.COL_INDEX)










if __name__ == "__main__":
    B = [[ 7, 0, 0 ],
         [ 0, 0, 0 ],
         [ 0, 0, 1 ]]
    A = [[1],[2],[3]]
    spA=SparseMatrix.array2sp(A)
    spB =SparseMatrix.array2sp(B)
    spA.display()
    spB.display()
    spA.transpose()
    spA.display()







