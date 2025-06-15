# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 00:03:14 2025

@author: jwang

Problem Description:
    An image smoother is a filter of the size 3 x 3 that can be applied to each 
    cell of an image by rounding down the average of the cell and the eight 
    surrounding cells.  If one or more of the surrounding cells of a cell is 
    not present, we do not consider it in the average.  

Important Constraints:
    m == img.length
    n == img[i].length
    1 <= m, n <= 200
    0 <= img[i][j] <= 255
"""

def imageSmoother(img):
    """
    :type img: List[List[int]]
    :rtype: List[List[int]]
    """
    if len(img[0]) == 1 and len(img) == 1:  #edge case: 1x1 matrix which has no neighbors
        return img  #return the input itself

    smoothened_image = []
    for r in range(len(img)):
        nested_list = []
        for c in range(len(img[r])):
            nested_list.append(0)
        smoothened_image.append(nested_list)

    if len(img) == 1:   #special case: if there is only row in a matrix
        for c in range(len(img[0])):
            if c == 0:  #leftmost column only has a right neighbor
                smoothened_image[0][c] = (img[0][c] + img[0][c + 1]) // 2
            elif c == len(img[0]) - 1:  #rightmost column only has a left neighbor
                smoothened_image[0][c] = (img[0][c] + img[0][c - 1]) // 2                    
            else:   #has a left and right neighbor
                smoothened_image[0][c] = (img[0][c - 1] + img[0][c] + img[0][c + 1]) // 3 
        return smoothened_image

    if len(img[0]) == 1:    #Another special case: matrix only has one column
        for r in range(len(img)):
            if r == 0:  #topmost row only has a bottom neighbor
                smoothened_image[r][0] = (img[r + 1][0] + img[r][0]) // 2
            elif r == len(img) - 1: #bottommost row only has a top neighbor
                smoothened_image[r][0] = (img[r - 1][0] + img[r][0]) // 2
            else:   #has a top and borrom neighbor
                smoothened_image[r][0] = (img[r - 1][0] + img[r][0] + img[r + 1][0]) // 3
        return smoothened_image

    for r in range(len(img)):
        for c in range(len(img[r])):
            if r == 0 and c == 0:   #top left corner case
                smoothened_image[r][c] = (img[r][c] + img[r][c + 1] + img[r + 1][c] + img[r + 1][c + 1]) // 4
            elif r == 0 and c == len(img[r]) - 1:   #top right corner case
                smoothened_image[r][c] = (img[r][c] + img[r][c - 1] + img[r + 1][c] + img[r + 1][c - 1]) // 4                  
            elif r == len(img) - 1 and c == 0:  #bottom left corner case
                smoothened_image[r][c] = (img[r][c] + img[r - 1][c] + img[r - 1][c + 1] + img[r][c + 1]) // 4                   
            elif r == len(img) - 1 and c == len(img[r]) - 1:    #bottom right corner case
                smoothened_image[r][c] = (img[r][c] + img[r - 1][c] + img[r - 1][c - 1] + img[r][c - 1]) // 4                 
            elif r == 0:    #topmost row
                smoothened_image[r][c] = (img[r][c] + img[r][c - 1] + img[r][c + 1] + img[r + 1][c] 
                + img[r + 1][c - 1] + img[r + 1][c + 1]) // 6
            elif r == len(img) - 1:     #bottom most row
                smoothened_image[r][c] = (img[r][c] + img[r][c - 1] + img[r][c + 1] + img[r - 1][c] 
                + img[r - 1][c - 1] + img[r - 1][c + 1]) // 6
            elif c == 0:    #leftmost column
                smoothened_image[r][c] = (img[r][c] + img[r - 1][c] + img[r + 1][c] + img[r][c + 1] 
                + img[r - 1][c + 1] + img[r + 1][c + 1]) // 6
            elif c == len(img[r]) - 1:  #rightmost column
                smoothened_image[r][c] = (img[r][c] + img[r - 1][c] + img[r + 1][c] + img[r][c - 1] 
                + img[r - 1][c - 1] + img[r + 1][c - 1]) // 6
            else:   # not touching any edge of the matrix
                smoothened_image[r][c] = (img[r][c] + img[r][c - 1] + img[r][c + 1] + img[r - 1][c - 1] + img[r - 1][c] + img[r - 1][c + 1] 
                + img[r + 1][c - 1] + img[r + 1][c] + img[r + 1][c + 1]) // 9

    return smoothened_image

img = [[1,1,1],[1,0,1],[1,1,1]]
print("The smoothened image of", img, ":", imageSmoother(img))

img2 = [[100,200,100],[200,50,200],[100,200,100]]
print("The smoothened image of", img2, ":", imageSmoother(img2))

img3 = [[100,200,100],[200,50,200],[100,200, 100], [100, 100, 100]]
print("The smoothened image of", img3, ":", imageSmoother(img3))

img4 = [[1]]
print("The smoothened image of", img4, ":", imageSmoother(img4))

img5 = [[2,3]]
print("The smoothened image of", img5, ":", imageSmoother(img5))

img6 = [[3],[2]]
print("The smoothened image of", img6, ":", imageSmoother(img6))

