def get_answer(heights):
    if heights[0] <= heights[1] <= heights[2] <= heights[3] or heights[0] >= heights[1] >= heights[2] >= heights[3]:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    heights_inp = list(map(int, input().split()))
    print(get_answer(heights_inp))
