# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 22:26:31 2025

@author: jwang

Problem Description:
    You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
    Your task is to transform this absolute path into its simplified canonical path.
    
    The rules of a Unix-style file system are as follows:
    
        - A single period '.' represents the current directory.
        - A double period '..' represents the previous/parent directory.
        - Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
        - Any sequence of periods that does not match the rules above should be treated as 
          a valid directory or file name. For example, '...' and '....' are valid directory or file names.
    
    The simplified canonical path should follow these rules:
    
        - The path must start with a single slash '/'.
        - Directories within the path must be separated by exactly one slash '/'.
        - The path must not end with a slash '/', unless it is the root directory.
        - The path must not have any single or double periods ('.' and '..') used to
          denote current or parent directories.
    
    Return the simplified canonical path.

Constraints:
    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/' or '_'.
    path is a valid absolute Unix path.
"""

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    path_sectors = path.split('/')
    i = 0
    while(i < len(path_sectors)):
        if path_sectors[i] == '':
            path_sectors.remove('')
        else:
            i += 1
    
    simplified_path = "/"
    theStack = []
    for j in range(len(path_sectors)):
        if path_sectors[j] == '.':  #current directory
            continue
        elif path_sectors[j] == '..':   #parent_directory
            if len(theStack) > 0:
                theStack.pop()  #go up a directory
        else:
            theStack.append(path_sectors[j])
    
    for j in range(len(theStack)):
        if j != len(theStack) - 1:
            simplified_path = simplified_path + theStack[j] + '/'
        else:   #path cannot end with a slash unless it is the root directory
            simplified_path = simplified_path + theStack[j]

    return simplified_path

path = "/home/"
#All trailing slash must be removed, unless it is root directory
print(simplifyPath(path))   #Output: "/home" 

path2 = "/home//foo/"
# multiple consecutive slashes are replaced by a single slash.
print(simplifyPath(path2))  #Output: "/home/foo"

path3 = "/home/user/Documents/../Pictures"
#double period refers to directory up a level
print(simplifyPath(path3))  #Output: "/home/user/Pictures"

path4 = "/../"
#going one level up from the root directory is not possible
print(simplifyPath(path4))  #Ouput: "/"

path5 = "/.../a/../b/c/../d/./"
print(simplifyPath(path5))  #Output: "/.../b/d"


