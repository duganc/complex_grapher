import unittest
from approvaltests.Approvals import verify
from approvaltests.GenericDiffReporterFactory import GenericDiffReporterFactory
import grapher

class ComplexGrapherTests(unittest.TestCase):

    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get('BeyondCompare4Mac')

    def test_plot_single_point(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(1, -4))
        png = cg.save_as_png("test_plot_single_point")
        verify(str(hash(png)), self.reporter)

    def test_plot_several_points(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(2, -1))
        cg.add_point(complex(-3, 2))
        cg.add_point(complex(-1, 1))
        cg.add_point(complex(-4, 7))
        png = cg.save_as_png("test_plot_several_points")
        verify(str(hash(png)), self.reporter)

    def test_plot_labeled_points(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(2, -1), label=True)
        cg.add_point(complex(-3, 2))
        cg.add_point(complex(-1, 1))
        cg.add_point(complex(-4, 7), label=True)
        png = cg.save_as_png("test_plot_labeled_points")
        verify(str(hash(png)), self.reporter)

    def test_plot_triangled_points(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(2, -1), label=True, triangle=True)
        cg.add_point(complex(-3, 2))
        cg.add_point(complex(-1, 1), triangle=True)
        cg.add_point(complex(-4, 7), label=True)
        png = cg.save_as_png("test_plot_triangled_points")
        verify(str(hash(png)), self.reporter)

    def test_add_arrow(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(2, -1))
        cg.add_point(complex(-3, 2))
        cg.add_arrow(complex(2, -1), complex(-3, 2))
        png = cg.save_as_png("test_plot_points_with_arrows")
        verify(str(hash(png)), self.reporter)

    def test_arrowed_point(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(2, -1), label=True, triangle=True)
        cg.add_point(complex(-3, 2), arrow=True)
        cg.add_point(complex(-1, 1), triangle=True)
        cg.add_point(complex(-4, 7), label=True, arrow=True)
        png = cg.save_as_png("test_plot_arrowed_points")
        verify(str(hash(png)), self.reporter)

    def test_arc_arrowed_point(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(-3, 2), label=True, arc_angle=True)
        cg.add_point(complex(1, 1), label=True, arc_angle=True)
        png = cg.save_as_png("test_plot_arc_arrowed_points")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_1(self):
        cg = grapher.ComplexGrapher()
        cg.add_point(complex(2, 1), label=True)
        cg.add_point(complex(-3, 2), label=True)
        png = cg.save_as_png("trig_post_figure_1_two_labeled_points")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_2(self):
        cg = grapher.ComplexGrapher()
        z0 = complex(2, 1)
        z1 = complex(-3, 2)
        cg.add_point(z0, label=True)
        cg.add_point(z1, label=True)
        cg.add_point(z0 + z1, label=True, color='r')
        cg.add_arrow(complex(0, 0), z1)
        cg.add_arrow(z0, z0 + z1)
        png = cg.save_as_png("trig_post_figure_2_two_points_and_their_sum")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_3(self):
        cg = grapher.ComplexGrapher()
        z0 = complex(2, 1)
        z1 = complex(-3, 2)
        cg.add_point(z0, label=True)
        cg.add_point(z1, label=True)
        cg.add_point(z0*z1, label=True, color='r')
        png = cg.save_as_png("trig_post_figure_3_two_points_and_their_product")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_4(self):
        cg = grapher.ComplexGrapher()
        z0 = complex(0, 2)
        z1 = complex(-3, 2)
        cg.add_point(z0, label=True)
        cg.add_point(z1, label=True)
        cg.add_point(z0*z1, label=True, color='r')
        png = cg.save_as_png("trig_post_figure_4_multiplication_by_pure_imaginary")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_5(self):
        cg = grapher.ComplexGrapher()
        z0 = complex(0, -2)
        z1 = complex(-3, 2)
        cg.add_point(z0, label=True)
        cg.add_point(z1, label=True)
        cg.add_point(z0*z1, label=True, color='r')
        png = cg.save_as_png("trig_post_figure_5_multiplication_by_pure_negative_imaginary")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_6(self):
        cg = grapher.ComplexGrapher()
        cg.illustrate_multiplication(complex(0, 2), complex(-3, 2))
        png = cg.save_as_png("trig_post_figure_6_multiplication_by_pure_imaginary_illustrated")
        verify(str(hash(png)), self.reporter)

    def test_trig_post_figure_7(self):
        cg = grapher.ComplexGrapher()
        cg.illustrate_multiplication(complex(0, -2), complex(-3, 2))
        png = cg.save_as_png("trig_post_figure_7_multiplication_by_pure_negative_imaginary_illustrated")
        verify(str(hash(png)), self.reporter)

    def test_illustrate_multiplication(self):
        cg = grapher.ComplexGrapher()
        cg.illustrate_multiplication(complex(2, 1), complex(-3, 2))
        png = cg.save_as_png("test_illustrates_multiplication")
        verify(str(hash(png)), self.reporter)