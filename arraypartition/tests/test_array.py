__author__    = "Daniel Westwood"
__contact__   = "daniel.westwood@stfc.ac.uk"
__copyright__ = "Copyright 2024 United Kingdom Research and Innovation"

import numpy as np

from arraypartition import ArrayPartition

class TestArray:
    def test_array(self):

        # Example Array Partition

        array_part = ArrayPartition(
            'arraypartition/tests/data/example1.0.nc',
            'p',
        )

        assert array_part.shape == (2,180,360), "Shape Source Error"
        
        ap = array_part[0, slice(100,120), slice(100,120)]

        assert ap.shape == (1,20,20), "Shape Error"

        assert (np.array(array_part)[0][5][0] - 0.463) < 0.001, "Data Error"
        assert (np.array(ap)[0][5][0] - 0.803) < 0.001, "Data Error"

if __name__ == '__main__':
    TestArray().test_array()