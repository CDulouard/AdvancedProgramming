def primenumber(nb_to_return):
    number = 0
    count = 0
    yield number
    while count < nb_to_return:
        is_prime = True;
        number += 1
        for i in range(number // 2):
            if number % (i + 2) == 0:
                is_prime = False
                break
                break
        if is_prime:
            count += 1
            yield number

