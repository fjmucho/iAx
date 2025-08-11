from numpy import mean, std

def normalizer_features(data) -> tuple:
    """
    Parameters
    ----------
        data: Numpy array, data training 
    outputs 
    -------
        data_normal ..: Normalized data
        data_mean ....: Mean of each array
        data_std .....: standard deviation of each array
    """
    dta_mean = mean(data, axis=0)
    dta_std = std(data, axis=0)
    dta_normal = (data - dta_mean) / dta_std

    return (dta_normal, dta_mean, dta_std)

def eval_cost(x, y, w, b):
    pass 