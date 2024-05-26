#not solved, this is wrong
from collections import defaultdict
def is_symmetric(points):
    """
    Checks if a given 2D shape (defined by a set of coordinates) is symmetric.
    
    Parameters:
        points (list of tuple): List of (x, y) coordinates representing the shape.
        
    Returns:
        bool: True if the shape is symmetric, False otherwise.
    """
    if not points:
        return False

    # Calculate the center of mass
    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)
    
    # Check symmetry for each point
    point_set = set(points)
    for x, y in points:
        # Check symmetric points across the center of mass
        sx = 2 * cx - x
        sy = 2 * cy - y
        if (sx, sy) not in point_set:
            return False
    
    return True
def get_center_of_mass(points):
    """
    Checks if a given 2D shape (defined by a set of coordinates) is symmetric.
    
    Parameters:
        points (list of tuple): List of (x, y) coordinates representing the shape.
        
    Returns:
        bool: True if the shape is symmetric, False otherwise.
    """
    if not points:
        return False

    # Calculate the center of mass
    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)
    
    #print("cx,cy=%f,%f"%(cx,cy))
    return (cx,cy)
def flip_shape(points):
    """
    Flips a given 2D shape horizontally and vertically.
    
    Parameters:
        points (list of tuple): List of (x, y) coordinates representing the shape.
        
    Returns:
        tuple: Two lists of (x, y) coordinates representing the horizontally
               and vertically flipped shapes respectively.
    """
    if not points:
        return [], []

    # Find the min and max x and y values to determine the center of the shape
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for y, y in points)
    max_y = max(y for y, y in points)

    # Calculate the center line for horizontal and vertical flips
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    # Horizontal flip (reflect across the vertical center line)
    horizontal_flip = [((2 * center_x - x), y) for x, y in points]

    # Vertical flip (reflect across the horizontal center line)
    vertical_flip = [(x, (2 * center_y - y)) for x, y in points]

    return horizontal_flip, vertical_flip
def most_upper_left_coordinate(points):
    """
    Finds the most upper-left coordinate from a list of 2D coordinates.
    
    Parameters:
        points (list of tuple): List of (x, y) coordinates.
        
    Returns:
        tuple: The most upper-left coordinate.
    """
    if not points:
        return None

    # Initialize with the first point
    upper_left = points[0]

    for point in points:
        x, y = point
        ul_x, ul_y = upper_left

        # Check if this point is more upper or (in case of tie) more left
        if (y < ul_y) or (y == ul_y and x < ul_x):
            upper_left = point

    return upper_left
class Solution:
    
    def solve(self,n:int,m:int,grid:list):
        shapes=defaultdict(set)
       
        for i in range(n):
            for j in range(m):
                
                shapes[grid[i][j]].add((i,j))
                shapes[grid[i][j]].add((i+1,j))
                shapes[grid[i][j]].add((i,j+1))
                shapes[grid[i][j]].add((i+1,j+1))
                #record the anchor
                

        # translate shapes to meet (0,0)
        translated_shapes=[]
        for k in shapes:
            i,j=most_upper_left_coordinate(list(shapes[k]))
            cur=[]
            for e in shapes[k]:
                cur.append((e[0]-i,e[1]-j))
            cur.append("key=%d,%d"%(i,j))
            translated_shapes.append(cur.copy())
        
        # check cm between horizontally reflected shape
        for points in translated_shapes:
            key=points[-1]
            points.pop(-1)

            if is_symmetric(points):continue
            horizontal_flip, vertical_flip=flip_shape(points)
            cm=get_center_of_mass(points)
            cm_hf=get_center_of_mass(horizontal_flip)
            cm_vf=get_center_of_mass(vertical_flip)
            if cm!=cm_hf and cm!=cm_vf:return False
             
                
            
        return True



        

if __name__ == "__main__":
    s = Solution()

    arr=input().strip().split(' ')
    for i in range(2):
        arr[i]=int(arr[i])
    n,m=arr[0],arr[1]
    grid=[]
    for i in range(n):
        line=input().strip().split(' ')
        for i in range(m):line[i]=int(line[i])
        grid.append(line.copy())
    res=s.solve(n,m,grid)
    if res:print("Yes")
    else:print("No")
    