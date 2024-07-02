import click
import numpy as np

@click.command()
@click.option('-i', '--inputs', default = '()[]{}')
def main(inputs):

    s_arr = np.array([s_indi for s_indi in inputs], dtype = object)
    s_len = len(s_arr)
    #if s_len % 2 != 0:
    #    print(False)
    #    return

    temp_f = np.array(['(', '[', '{'], dtype = object)
    temp_b = np.array([')', ']', '}'], dtype = object)
    result = np.full((s_len), False, dtype = bool)
    for idx, s_indi in enumerate(s_arr):
        f_bool = temp_f == s_indi
        if np.any(f_bool):
            temp_l = temp_b[f_bool]
            pair_is = np.arange(idx + 1, s_len, 2, dtype = int)
        
        b_bool = temp_b == s_indi
        if np.any(b_bool):
            temp_l = temp_f[b_bool]
            pair_is = np.arange(idx - 1, -1, -2, dtype = int)
        
        pair_ls = s_arr[pair_is]          
        result[idx] = np.any(pair_ls == temp_l)            
        print(f'Test: {s_indi}, Expected: {temp_l}, Selected: {pair_ls}, Result: {result[idx]}')

    print(result) 
    print(np.all(result)) 

 
if __name__ == "__main__":
    main()
