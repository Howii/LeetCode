def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l = 0
    r = len(height) - 1
    area_max = 0
    while l < r:
        h = min(height[l], height[r])
        area_max = max(area_max, h * (r - l))
        while height[l] <= h and l < r:
            l += 1
        while height[r] <= h and l < r:
            r -= 1
    return area_max
