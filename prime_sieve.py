def prime_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range (2, n + 1, 1):
        if primes[i]:
            for j in range (i + i, n + 1, i):
                primes[j] = False;
    return primes
def main():
    print(prime_sieve(10))

if __name__ == "__main__":
  main()