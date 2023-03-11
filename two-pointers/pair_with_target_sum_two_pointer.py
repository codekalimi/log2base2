# Using two pointers
def hasPairWithTarget(arr, n, target):
    start = 0
    end = n - 1
    while start < end:
        total = arr[start] + arr[end]
        if total == target:
            return 1
        elif total < target:
            start = start + 1
        else:
            end = end - 1
    return 0


if __name__ == '__main__':
    arr = [1, 5, 10, 20, 80]
    target = 90
    print(hasPairWithTarget(arr, len(arr), target))

    arr = [1, 5, 10, 20, 80]
    target = 40
    print(hasPairWithTarget(arr, len(arr), target))

    arr = [-2, -1, 5, 13, 17, 25, 40]
    target = -3
    print(hasPairWithTarget(arr, len(arr), target))

    arr = [-2, -1, 5, 13, 17, 25, 40]
    target = 100
    print(hasPairWithTarget(arr, len(arr), target))

    arr = [-2, -1, 5, 13, 17, 25, 40]
    target = 39
    print(hasPairWithTarget(arr, len(arr), target))
