import click
import numpy as np
from scipy.ndimage import uniform_filter1d

@click.command()
@click.option('-i1', '--input1', default = '1, 1, 1, 2, 1, 2, 2, 2, 3, 3, 3')
@click.option('-i2', '--input2', default = 3)
def main(input1, input2):

    arr = np.asarray(input1.split(','), dtype = int)
    print(arr)

    arr_mean = uniform_filter1d(arr.astype(float), input2)
    print(arr_mean)

    diff = arr - arr_mean
    print(diff)

    num_con = np.unique(arr[diff == 0]) # I dont like this. Using float is unstable way
    print(num_con)

if __name__ == "__main__":
    main()




