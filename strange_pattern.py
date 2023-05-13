import numpy as np

# implement the function strange pattern

def strange_pattern(shape = (3,3)):
    pattern = np.zeros(shape, dtype=bool)
    pattern[::3,::3] = True
    pattern[1::3,2::3] = True
    pattern[2::3,1::3] = True
    return pattern


if __name__ == "__main__":
    # use this for your own testing!
    print(type(strange_pattern((10,10)))is np.ndarray)
    print(strange_pattern((5,8)))
    print(strange_pattern((2,2)))

    pass
