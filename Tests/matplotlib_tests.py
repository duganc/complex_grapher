import unittest
import numpy as np
import matplotlib


class MatPlotLibTests(unittest.TestCase):

    def test_installed(self):
        version = matplotlib.__version__
        self.assertIsNotNone(version)