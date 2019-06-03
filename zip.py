def test_zip():
    l1 = [i for i in range(100)]
    l2 = [i + 100 for i in range(100)]
    for i, j in enumerate(zip(l1, l2)):
        print(i, j)