if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort();
    arr = arr[::-1]
    for i in range(n):
        if (arr[i] != arr[0]):
            print(arr[i])
            break



