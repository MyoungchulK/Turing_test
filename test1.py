import click
import numpy as np

@click.command()
@click.option('-i', '--inputs', default = '2, 5, 6, 9')
def main(inputs):
    arr_list = np.asarray(inputs.split(','), dtype = int)

    arr_sort = np.sort(arr_list)
    arr_range = np.arange(1, len(arr_list) + 1, 1, dtype = int)
    print(arr_sort)
    print(arr_range)    

    arr_diff = arr_sort - arr_range
    print(arr_diff)

    arr_max = np.nansum(np.abs(arr_diff))
    print(arr_max)

 
if __name__ == "__main__":
    main()
