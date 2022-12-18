def find_primes(n):
    # Create a list of integers from 2 to n
    primes = [True] * (n + 1)

    # Set 0 and 1 to not be prime
    primes[0] = primes[1] = False

    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]
