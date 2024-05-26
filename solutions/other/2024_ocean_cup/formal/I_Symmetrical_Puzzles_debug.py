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
    
    print("cx,cy=%f,%f"%(cx,cy))
    # Check symmetry for each point
    point_set = set(points)
    for x, y in points:
        # Check symmetric points across the center of mass
        sx = 2 * cx - x
        sy = 2 * cy - y
        if (sx, sy) not in point_set:
            return False
    return True

'''
x
xxx 
'''
points = [(0,0),(0,1), 
          (1,0),(1,1),(1,2),(1,3),
          (2,0),(2,1),(2,2),(2,3)]
print(is_symmetric(points))

'''
  x
xxx 
'''
points = [            (0,2),(0,3) ,
          (1,0),(1,1),(1,2),(1,3),
          (2,0),(2,1),(2,2),(2,3)]
print(is_symmetric(points))

'''
 xx
xx 
'''
points = [      (0,1),(0,2),(0,3),
          (1,0),(1,1),(1,2),(1,3),
          (2,0),(2,1),(2,2)    ]
print(is_symmetric(points))

'''
xx
 xx 
'''
points = [(0,0),(0,1),(0,2),
          (1,0),(1,1),(1,2),(1,3),
                (2,1),(2,2),(2,3)  ]
print(is_symmetric(points))