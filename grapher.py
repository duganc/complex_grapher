import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

class ComplexGrapher:

    def __init__(self, show_unit_circle = False):
        assert type(show_unit_circle) == bool
        self.show_unit_circle = show_unit_circle

        self.xmin = -10
        self.xmax = 10
        self.ymin = -10
        self.ymax = 10

        self.real_coords = list()
        self.imag_coords = list()
        self.labels = list()
        self.triangles = list()
        self.point_arrows = list()
        self.arc_arrows = list()

        self.arrows = list()


    def add_point(self, z, label = False, triangle = False, arrow = False, arc_angle = False):
        assert type(z) == complex
        assert type(label) == bool
        assert type(triangle) == bool
        assert type(arrow) == bool
        assert type(arc_angle) == bool

        self.real_coords.append(z.real)
        self.imag_coords.append(z.imag)
        self.labels.append(label)
        self.triangles.append(triangle)
        self.point_arrows.append(arrow)
        self.arc_arrows.append(arc_angle)

    def add_arrow(self, start, end):
        assert type(start) == complex
        assert type(end) == complex

        self.arrows.append([[start.real, start.imag], [end.real, end.imag]])

    def illustrate_multiplication(self, c1, c2):
        assert type(c1) == complex
        assert type(c2) == complex

        self.add_point(c1, label = True, arc_angle = True, arrow = True)
        self.add_point(c2, label=True, arc_angle=True, arrow = True)
        self.add_point(c1 * c2, label=True, arc_angle=True, arrow = True)

    def set_axes(self, xmin, xmax, ymin, ymax):
        assert type(xmin) == int
        assert type(xmax) == int
        assert type(ymin) == int
        assert type(ymax) == int
        assert xmin < xmax
        assert ymin < ymax

        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def show(self):

        self._plot()

        plt.show()

    def save_as_png(self, path):
        assert type(path) == str

        self._plot()

        path_w_suffix = path + ".png"

        return plt.savefig(path)

    def _plot(self):

        figure, axes = plt.subplots()

        plt.xlabel('Real')
        plt.ylabel('Imaginary')

        plt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        plt.xticks(np.arange(self.xmin, self.xmax + 1, 1.0))
        plt.yticks(np.arange(self.ymin, self.ymax + 1, 1.0))
        axes.grid(True, which='both')

        axes.axhline(y=0, color='k')
        axes.axvline(x=0, color='k')

        axes.plot(self.real_coords, self.imag_coords, 'o')

        i = 0
        arc_arrow_count = 0
        for xy in zip(self.real_coords, self.imag_coords):
            if (self.labels[i]):
                axes.annotate('  %s + %si' % xy, xy=xy, textcoords = 'data', fontsize = 10)
            if (self.triangles[i]):
                polygon = patches.Polygon(
                    [
                        [0, 0],
                        [xy[0], xy[1]],
                        [xy[0], 0]
                    ],
                    True,
                    fill = None,
                    edgecolor = 'g'
                )
                axes.add_patch(polygon)
                r_sqrd = round(xy[0] * xy[0] + xy[1] * xy[1])
                r_label_x = xy[0] / 2 - 0.25
                r_label_y = 2.1 * xy[1] / 2
                if (r_label_y < 0):
                    r_label_y = r_label_y * 1.1 #Pad to keep the sqrt from hitting the triangle.
                axes.annotate(r"$\sqrt{%s}$" % r_sqrd, xy = (r_label_x, r_label_y), color = "g", fontsize = 8)
            if (self.point_arrows[i]):
                self.add_arrow(complex(0, 0), complex(self.real_coords[i], self.imag_coords[i]))
            if (self.arc_arrows[i]):
                arc_arrow_count += 1
                self.add_arrow(complex(0, 0), complex(self.real_coords[i], self.imag_coords[i]))
                angle_in_rads = math.atan2(self.imag_coords[i], self.real_coords[i])
                arc = patches.Arc((0, 0), 0.5 * arc_arrow_count, 0.5 * arc_arrow_count, 0, 0, math.degrees(angle_in_rads))
                axes.add_patch(arc)
            i += 1

        for arrow in self.arrows:
            HEAD_WIDTH = 0.25
            HEAD_LENGTH = 0.5
            xlength = (arrow[1][0] - arrow[0][0])
            ylength = (arrow[1][1] - arrow[0][1])
            angle = math.atan2(ylength, xlength)
            axes.arrow(arrow[0][0], arrow[0][1], xlength, ylength, head_width=HEAD_WIDTH, head_length=HEAD_LENGTH, fc='b', ec='b', length_includes_head=True)