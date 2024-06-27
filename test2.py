import click
import numpy as np
from more_itertools import substrings

@click.command()
@click.option('-i', '--inputs', default = '1, 2, 3')
def main(inputs):
    arr_list = np.asarray(inputs.split(','), dtype = int)

    arr_conti = list(map(list, substrings(arr_list)))
    print(arr_conti)

    arr_sum = []
    for a in arr_conti:
        arr_sum.append(sum([aa for aa in a]))
    print(arr_sum)

    arr_max = np.nanmax(np.asarray(arr_sum, dtype = int) ** 2)
    print(arr_max)

def main_2(inputs = '1, 2, 3'):
    arr_list = np.asarray(inputs.split(','), dtype = int)

    arr_len = len(arr_list)
    arr_sum_max = np.full((arr_len), 0, dtype = int)
    for a in range(arr_len):
        arr_con = np.convolve(arr_list, np.ones((a + 1), dtype = int), mode = 'valid')
        print(arr_con)
        arr_sum_max[a] = np.nanmax(arr_con ** 2)
    arr_max = np.nanmax(arr_sum_max)
    print(arr_max)


 
if __name__ == "__main__":
    main()
    #main_2()
