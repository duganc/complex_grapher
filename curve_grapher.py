import numpy as np
import matplotlib.pyplot as plt

class curve_grapher:

    def __init__(self):

        self.curve_plotted = False

    def save_as_png(self, path):
        assert type(path) == str
        assert self.curve_plotted

        path_w_suffix = path + ".png"

        return plt.savefig(path)

    def plot_curve(self, np_x, np_y, xmin = -10, xmax = 10, ymin = -10, ymax = 10, xlabel = "x", ylabel = "y"):
        assert isinstance(np_x, np.ndarray)
        assert isinstance(np_y, np.ndarray)
        self._assert_and_cast_int_to_float(xmin)
        self._assert_and_cast_int_to_float(xmax)
        self._assert_and_cast_int_to_float(ymin)
        self._assert_and_cast_int_to_float(ymax)
        assert type(xlabel) == str
        assert type(ylabel) == str

        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        figure, axes = plt.subplots()

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        plt.xticks(np.arange(self.xmin, self.xmax + 1, 1.0))
        plt.yticks(np.arange(self.ymin, self.ymax + 1, 1.0))
        axes.grid(True, which='both')

        axes.axhline(y=0, color='k')
        axes.axvline(x=0, color='k')

        axes.plot(np_x, np_y)

        self.curve_plotted = True

    def _assert_and_cast_int_to_float(self, x):
        assert type(x) == int or type(x) == float
        if type(x) == int:
            return float(x)

        return x