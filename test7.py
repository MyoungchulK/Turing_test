import click
import numpy as np

@click.command()
@click.option('-i', '--inputs', default = '1,2,3,4')
def main(inputs):

    arr = np.asarray(inputs.split(','), dtype = int)
    arr_len = len(arr)
    arr_range = np.arange(arr_len, dtype = int)
    print(arr)

    arr_2d = np.repeat(arr[:, np.newaxis], arr_len, axis = 1)
    arr_2d[arr_range, arr_range] = 1
    print(arr_2d)

    arr_prod = np.prod(arr_2d, axis = 0)
    print(arr_prod)

if __name__ == "__main__":
    main()




