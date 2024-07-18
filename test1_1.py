import click
import numpy as np

@click.command()
@click.option('-i', '--inputs', default = '0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0')
def main(inputs):
    arr_list = np.asarray(inputs.split(','), dtype = int)
    print(arr_list)

    arr_diff = np.abs(np.diff(arr_list))
    diff_len = len(arr_diff)
    print(arr_diff)

    arr_con = np.arange(diff_len, dtype = int) + 1
    for a in range(diff_len):
        temp_len = a + 1
        conv = np.convolve(arr_diff, np.ones((temp_len), dtype = int))
        print(temp_len, conv)

        if np.any(conv == temp_len): pass
        else: arr_con[a] = 0
    print(arr_con)

    output = np.nanmax(arr_con) + 1
    print(output)
 
if __name__ == "__main__":
    main()
