import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc=None, scale=None, lower_bound=None, upper_bound=None):
    if not isinstance(loc, int) and not isinstance(loc, float):
        raise TypeError("loc is not a number")
    elif not isinstance(scale, int) and not isinstance(scale, float):
        raise TypeError("scale is not a number")
    elif not isinstance(lower_bound, int) and not isinstance(lower_bound, float):
        raise TypeError("lower_bound is not a number")
    elif not isinstance(upper_bound, int) and not isinstance(upper_bound, float):
        raise TypeError("upper_bound is not a number")
    elif not lower_bound < upper_bound:
        raise TypeError("upper_bound is not smaller than lower_bound")
    
    sample = np.random.normal(loc=loc, scale=scale, size=100)
    filter_one = sample > lower_bound
    sample = sample[filter_one]
    filter_two = sample < upper_bound
    sample = sample[filter_two]
    mean = np.mean(sample)
    std = np.std(sample)
    return (mean, std)


if __name__ == "__main__":
    # use this for your own testing!
    print(gaussian_analysis(loc=5, scale=2, lower_bound=3, upper_bound=9))

    pass
