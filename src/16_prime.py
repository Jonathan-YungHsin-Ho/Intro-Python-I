import sys


def main():
    args_check()

    num = sys.argv[1]
    print_prime_status(num)


def args_check():
    if len(sys.argv) != 2:
        print(
            'Please call this program as follows: python 16_prime.py [number]')
        sys.exit()


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def print_prime_status(num):
    if is_prime(int(num)):
        print(f'{num} is a prime number!')
    else:
        print(f'{num} is not a prime number!')


main()
