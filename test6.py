import click
import numpy as np

@click.command()
@click.option('-i1', '--input1', default = '1, 1, 1, 2, 1, 2, 2, 2, 3, 3, 3')
@click.option('-i2', '--input2', default = 3)
def main(input1, input2):

    arr = np.asarray(input1.split(','), dtype = int)
    print(arr)

if __name__ == "__main__":
    main()




