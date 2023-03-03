if __name__ == "__main__":
    a = [8, 3, 1, 19, 14]
    y = 0
    for x in range(len(a)-1):
        for i in range(len(a)-y):
            if i == 0:
                continue
            if a[i-1] < a[i]:
                continue
            elif a[i-1] > a[i]:
                first = a[i-1]
                a[i-1] = a[i]
                a[i] = first
        y += 1
    print(a)
