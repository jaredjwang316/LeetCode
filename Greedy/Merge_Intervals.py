"""
Problem Description:
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping 
    intervals, and return an array of the non-overlapping intervals that cover all the 
    intervals in the input.  

Constraints:
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= starti <= endi <= 10^4
"""

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key = lambda x: x[0])    

    mergedIntervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= mergedIntervals[-1][1]:
            mergedIntervals[-1][1] = max(mergedIntervals[-1][1], intervals[i][1])
        else:
            mergedIntervals.append(intervals[i])

    return mergedIntervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]

intervals2 = [[1,4],[4,5]]
print(merge(intervals2))  # Output: [[1,5]]

intervals3 = [[4,7],[1,4]]
print(merge(intervals3))  # Output: [[1,7]]

intervals4 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals4))  # Output: [[1,10]]

intervals5 = [[2,3],[5,5],[2,2],[3,4],[3,4]]
print(merge(intervals5))  # Output: [[2,4],[5,5]]

intervals6 = [[0,0],[1,2],[5,5],[2,4],[3,3],[5,6],[5,6],[4,6],[0,0],[1,2],[0,2],[4,5]]
print(merge(intervals6))  # Output: [[0,6]]