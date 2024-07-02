import click
import numpy as np

@click.command()
#@click.option('-i', '--inputs', default = '1,2,3 4,5,6 7,8,9')
@click.option('-i', '--inputs', default = '1,2,3,4,5,6 7,8,9,10,11,12 13,14,15,16,17,18 19,20,21,22,23,24 25,26,27,28,29,30')
def main(inputs):

    arr_2d = np.array([i_indi.split(',') for i_indi in inputs.split(' ')], dtype = int)
    arr_sh = np.asarray(arr_2d.shape)
    print('Array:')
    print(arr_2d)
    print('Shape:', arr_sh) 
    if np.any(arr_sh == 1):
        print(arr_2d.flatten())
        return

    m_range = np.arange(arr_sh[0], 0, -1, dtype = int)[:arr_sh[1]]
    n_range = np.arange(arr_sh[1] - 1, 0, -1, dtype = int)[:arr_sh[0]]
    mn_range = np.stack([m_range, n_range]).flatten("F")
    mn_len = np.nansum(mn_range)
    mn_cum = np.append(0, np.nancumsum(mn_range))
    print('Spiral each arm length:')
    print(mn_range)

    r_idxs = np.full((2, mn_len), 0, dtype = int)
    for r in range(len(mn_range)):
        r_mo = r % 4
        r_eo = r % 2
        r_int = r // 4
        mn_i = mn_cum[r]
        mn_f = mn_cum[r + 1]
        if r_mo == 0 and r_eo == 0:
            r_idxs[0, mn_i:mn_f] = r_int
            r_idxs[1, mn_i:mn_f] = np.arange(0, mn_range[r], dtype = int) + r_int
        elif r_mo == 1 and r_eo == 1:
            r_idxs[0, mn_i:mn_f] = np.arange(1, mn_range[r] + 1, dtype = int) + r_int
            r_idxs[1, mn_i:mn_f] = -(r_int + 1)
        elif r_mo == 2 and r_eo == 0:
            r_idxs[0, mn_i:mn_f] = -(r_int + 1)
            r_idxs[1, mn_i:mn_f] = np.arange(mn_range[r] - 1, -1, -1, dtype = int) + r_int
        elif r_mo == 3 and r_eo == 1:
            r_idxs[0, mn_i:mn_f] = np.arange(mn_range[r], 0, -1, dtype = int) + r_int
            r_idxs[1, mn_i:mn_f] = r_int 
        else:
            pass
    print('Spiral index toward original array:')
    print(r_idxs) 
    result = arr_2d[r_idxs[1], r_idxs[0]]
    print('Reverse Spiral Result:')
    print(result) 

if __name__ == "__main__":
    main()




