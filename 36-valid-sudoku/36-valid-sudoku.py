class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            elem=[]            
            for j in row :
                if(j!="."):
                    if (j in elem):
                         
                        return False
                    else:
                        elem.append(j)
        
  
        for i in range(len(board)):
            elem =[] 
            for j in range(9):
                if(board[j][i] not in elem and board[j][i]!="."):
                    elem.append(board[j][i])
                elif (board[j][i]!="."):
                    return False
 
        
    
        for i in range(0,9,3):   
            for j in range(0,9,3) :
                elem=[]
                for k in range(i,i+3):                    
                    for l in range(j,j+3):
                        if(board[k][l] not in elem and board[k][l]!="."):
                            elem.append(board[k][l])
                        elif (board[k][l]!="."):
                            return False
                           
            
        return True

        
        
        