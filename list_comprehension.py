from generator import *


def test_l_c():
    work_list = [i for i in primenumber(1000)]

    incr_list = [i + 1 for i in work_list]

    end_by_nine = [i for i in work_list if i % 10 == 9]

    gene_comprehension = (i for i in work_list if i % 10 == 7)

    print(work_list)
    print(incr_list)
    print(end_by_nine)
    print([i for i in gene_comprehension])
    pass
