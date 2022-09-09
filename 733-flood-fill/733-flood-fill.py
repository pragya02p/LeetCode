class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        v=image[sr][sc]
        if v==color:
            return image
        def change_color(r,c): 
            if image[r][c]==v:
                image[r][c]=color
                if r>=1: change_color(r-1,c)
                if r+1<m: change_color(r+1,c)
                if c>=1: change_color(r,c-1)       
                if c+1<n: change_color(r,c+1)
                
        

        change_color(sr,sc)
        return image
                
    
        