if __name__ == '__main__':
    row1 = [1, 2, 3]
    row2 = [4, 5, 6]
    row3 = []
    row1.extend(row2)
    print(row1)
    print(row1+row2)
    row1.append(row2)
    print(row1)
    a = [[1,2,3],[4,5,6]]
    b = a.copy()
    c = []
    print(b)
    a.extend(b)
    print(a)
    c.extend(a)
    c.extend(b)
    print(c)

