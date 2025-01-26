import click
import numpy as np
from itertools import combinations

@click.command()
@click.option('-i', '--inputs', default = 5)
def main(inputs):

    arr = np.arange(inputs, dtype=int) + 1
    print(arr)

    com = np.asarray(list(combinations(arr, 3))).astype(int)
    print(com)

    com_sqrt = com ** 2

    sum_bool = np.nansum(com_sqrt[:, :2], axis=1) == com_sqrt[:, 2]
    print(sum_bool)

    sums = np.nansum(sum_bool) * 2
    print(com[sum_bool])
    print('sums:', sums)

if __name__ == "__main__":
    main()
