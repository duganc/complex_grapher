import numpy as np
import matplotlib.pyplot as plt
import unittest
from approvaltests.Approvals import verify
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory
import curve_grapher

class CurveGrapherTests(unittest.TestCase):

    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get('BeyondCompare4Mac')

    def test_generates_linear_plot(self):

        cg = curve_grapher.curve_grapher()
        x = np.linspace(-10, 10, 500)
        y = 2*x - 1

        cg.plot_curve(x, y)
        png = cg.save_as_png("linear_plot_test")

        verify(str(hash(png)), self.reporter)


    def test_e_post_figure_1(self):

        cg = curve_grapher.curve_grapher()
        x = np.linspace(0, 10, 500)

        cg.plot_curve(x, x/2, xmin = 0, ymin = 0, xlabel="Time (Time Units)", ylabel="Boredom (Boredom Units)")
        png = cg.save_as_png("e_post_figure_1_linear_boredom")

        verify(str(hash(png)), self.reporter)

    def test_e_post_figure_2(self):

        cg = curve_grapher.curve_grapher()
        x = np.linspace(0, 10, 500)

        cg.plot_curve(x, x / x / 2, xmin = 0, ymin = 0, xlabel="Time (Time Units)", ylabel="Boredom per Time (Boredom Units per Time Units)")
        png = cg.save_as_png("e_post_figure_2_slope_of_linear_boredom")

        verify(str(hash(png)), self.reporter)

    def test_e_post_figure_3(self):

        cg = curve_grapher.curve_grapher()
        x = np.linspace(0, 10, 500)

        cg.plot_curve(x, pow(x, 2)/4, xmin = 0, ymin = 0, xlabel="Time (Time Units)", ylabel="Boredom (Boredom Units)")
        png = cg.save_as_png("e_post_figure_3_quadratic_boredom")

        verify(str(hash(png)), self.reporter)

    def test_e_post_figure_4(self):

        cg = curve_grapher.curve_grapher()
        x = np.linspace(0, 10, 500)

        cg.plot_curve(x, x / 2, xmin = 0, ymin = 0, xlabel="Time (Time Units)", ylabel="Boredom per Time (Boredom Units per Time Units)")
        png = cg.save_as_png("e_post_figure_4_slope_of_quadratic_boredom")

        verify(str(hash(png)), self.reporter)


    def test_e_post_figure_8(self):
        cg = curve_grapher.curve_grapher()
        x = np.linspace(0, 10, 500)

        cg.plot_curve(x, np.exp(x), xmin=0, ymin=0, xlabel="Time (Time Units)", ylabel="Boredom (Boredom Units)")
        png = cg.save_as_png("e_post_figure_8_exponential_boredom")

        verify(str(hash(png)), self.reporter)