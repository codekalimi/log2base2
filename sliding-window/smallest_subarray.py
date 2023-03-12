import sys


def smallLengthSubarraySum(arr, n, S):
    wstart = 0
    len = sys.maxsize
    subSum = 0

    for i in range(n):
        subSum += arr[i]

        while subSum >= S:
            currentWindowSize = i - wstart + 1

            if currentWindowSize < len:
                len = currentWindowSize

            subSum -= arr[wstart]
            wstart += 1

    if len == sys.maxsize:
        return 0
    else:
        return len


if __name__ == '__main__':
    arr = [4, 1, 5, 2, 4, 1]
    S = 7
    print(smallLengthSubarraySum(arr, len(arr), S))
