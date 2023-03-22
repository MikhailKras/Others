def find_max_median(n, s, intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    left = min([l for l, r in intervals])
    right = max([r for l, r in intervals])
    max_median = left
    while left <= right:
        mid = (left + right) // 2
        current_sum = 0
        for i in range(n):
            if sorted_intervals[i][1] >= mid:
                current_sum += max(sorted_intervals[i][0], mid - (current_sum + sorted_intervals[i][1] - sorted_intervals[i][0]))
            else:
                current_sum = float('inf')
                break
        if current_sum <= s:
            max_median = mid
            left = mid + 1
        else:
            right = mid - 1
    return max_median


n, s = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
result = find_max_median(n, s, intervals)
print(result)
