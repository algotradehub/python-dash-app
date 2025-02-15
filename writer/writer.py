import time
import json
import random

import redis


def main():

    client = redis.Redis(host='redis', port=6379, db=0)
    counter = 0

    while True:

        numbers = [random.randint(1, 10) for _ in range(100)]

        client.hest(name='random', key='nums', value=json.dumps(numbers))
        counter += 1
        print(f"counter updated to {counter}")
        time.sleep(1)


if __name__ == '__main__':

    main()