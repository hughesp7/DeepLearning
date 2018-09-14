import numpy as np
def gen_data():
    x = np.arange(0, 25, 0.1);
    y = np.sin(x)
    return (x, y)