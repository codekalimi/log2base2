# Without two pointers
def hasPairWithTarget(arr, n, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) == target:
                return 1
    return 0


if __name__ == '__main__':
    arr = [1, 5, 10, 20, 80]
    target = 90
    print(hasPairWithTarget(arr, len(arr), target))
