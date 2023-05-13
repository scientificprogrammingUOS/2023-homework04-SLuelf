import numpy as np 

# implement your function to combine two numpy arrays 

def combination(ary_one, ary_two, axis=0):
    ary_one = np.squeeze(ary_one)
    ary_two = np.squeeze(ary_two)
    try:
        return np.concatenate((ary_one, ary_two), axis=axis)
    except:
        raise ValueError("The two arrays can not be combined along the given axis")
    


if __name__ == "__main__":
    print(combination([1,2],[3,4]))

    pass
