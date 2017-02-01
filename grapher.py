import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

class ComplexGrapher:

    def __init__(self):

        self.xmin = -10
        self.xmax = 10
        self.ymin = -10
        self.ymax = 10

        self.real_coords = list()
        self.imag_coords = list()
        self.labels = list()
        self.impute_sqrts = list()
        self.triangles = list()
        self.point_arrows = list()
        self.arc_arrows = list()
        self.colors = list()

        self.arrows = list()
        self.arrow_colors = list()

        self.circles = list()


    def add_point(self, z, label = False, impute_sqrt_label = False, triangle = False, arrow = False, arc_angle = False, color = 'b'):
        assert type(z) == complex
        assert type(label) == bool
        assert type(impute_sqrt_label) == bool
        assert type(triangle) == bool
        assert type(arrow) == bool
        assert type(arc_angle) == bool
        assert type(color) == str

        self.real_coords.append(z.real)
        self.imag_coords.append(z.imag)
        self.labels.append(label)
        self.impute_sqrts.append(impute_sqrt_label)
        self.triangles.append(triangle)
        self.point_arrows.append(arrow)
        self.arc_arrows.append(arc_angle)
        self.colors.append(color)

    def add_arrow(self, start, end, color = 'b'):
        assert type(start) == complex
        assert type(end) == complex
        assert type(color) == str

        self.arrows.append([[start.real, start.imag], [end.real, end.imag]])
        self.arrow_colors.append(color)

    def add_circle(self, radius, center):
        if type(radius) == int:
            radius = float(radius)
        assert type(radius) == float
        assert type(center) == complex
        assert radius > 0

        self.circles.append([radius, [center.real, center.imag]])

    def illustrate_multiplication(self, c1, c2, impute_sqrt_labels = False):
        assert type(c1) == complex
        assert type(c2) == complex
        assert type(impute_sqrt_labels) == bool

        self.add_point(c1, label = True, impute_sqrt_label=impute_sqrt_labels, arc_angle = True)
        self.add_point(c2, label=True, impute_sqrt_label=impute_sqrt_labels, arc_angle=True)
        self.add_point(c1 * c2, label=True, impute_sqrt_label=impute_sqrt_labels, arc_angle=True, color='r')

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

        i = 0
        arc_arrow_count = 0
        for xy in zip(self.real_coords, self.imag_coords):
            axes.plot(self.real_coords[i], self.imag_coords[i], 'o', color=self.colors[i])
            if (self.labels[i]):
                xy_label = (round(xy[0], 3), round(xy[1], 3))
                if (self.impute_sqrts[i]):
                    xy_label = (self.impute_sqrt_label(xy_label[0], sqrt_decimals=2, pass_thru_decimals=2), self.impute_sqrt_label(xy_label[1], sqrt_decimals=2, pass_thru_decimals=2))
                axes.annotate('  %s + %si' % xy_label, xy=xy, textcoords = 'data', fontsize = 10)
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
                self.add_arrow(complex(0, 0), complex(self.real_coords[i], self.imag_coords[i]), self.colors[i])
            if (self.arc_arrows[i]):
                arc_arrow_count += 1
                self.add_arrow(complex(0, 0), complex(self.real_coords[i], self.imag_coords[i]), self.colors[i])
                angle_in_rads = math.atan2(self.imag_coords[i], self.real_coords[i])
                arc = patches.Arc((0, 0), 0.5 * arc_arrow_count, 0.5 * arc_arrow_count, 0, 0, math.degrees(angle_in_rads))
                axes.add_patch(arc)
            i += 1

        i = 0
        for arrow in self.arrows:
            HEAD_WIDTH = 0.25
            HEAD_LENGTH = 0.5
            xlength = (arrow[1][0] - arrow[0][0])
            ylength = (arrow[1][1] - arrow[0][1])
            angle = math.atan2(ylength, xlength)
            axes.arrow(
                arrow[0][0],
                arrow[0][1],
                xlength,
                ylength,
                head_width=HEAD_WIDTH,
                head_length=HEAD_LENGTH,
                fc=self.arrow_colors[i],
                ec=self.arrow_colors[i],
                length_includes_head=True
            )
            i += 1

        for circle_dims in self.circles:
            circle = patches.Circle(circle_dims[1], circle_dims[0], fill=None, color='b')
            axes.add_patch(circle)

        axes.set_aspect('equal', 'datalim')


    def impute_sqrt_label(self, x, pass_thru_decimals = 3, sqrt_decimals = 0):
        if type(x) == int:
            x = float(x)
        assert type(x) == float
        assert type(pass_thru_decimals) == int
        assert pass_thru_decimals >= 0
        assert type(sqrt_decimals) == int
        assert sqrt_decimals >= 0

        if round(x, pass_thru_decimals) == x:
            return str(x)

        x_sqrd = x*x
        rounded_x_sqrd = round(x_sqrd, sqrt_decimals)
        tolerence = pow(0.1, sqrt_decimals + 1)
        if (math.fabs(rounded_x_sqrd - x_sqrd) < tolerence):
            return str(r"$\sqrt{%s}$" % rounded_x_sqrd)

        return str(x)
