import click
import numpy as np

@click.command()
@click.option('-i1', '--input1', default = 'leetcode')
@click.option('-i2', '--input2', default = 3)
def main(input1, input2):

    temp = np.array(['a', 'e', 'i', 'o', 'u'], dtype = 'object')
    s_list = np.array([s_indi for s_indi in input1], dtype = 'object')
    s_bool = np.in1d(s_list, temp).astype(int)
    print(s_list)
    print(temp)
    print(s_bool)
    
    sub_sum = np.convolve(s_bool, np.ones((input2), dtype = int), mode = 'valid')
    sub_max = np.nanmax(sub_sum)
    print(sub_max)

if __name__ == "__main__":
    main()




