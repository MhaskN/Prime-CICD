def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    print("First 5 prime numbers:", generate_primes(5))
