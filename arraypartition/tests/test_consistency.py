__author__    = "Daniel Westwood"
__contact__   = "daniel.westwood@stfc.ac.uk"
__copyright__ = "Copyright 2024 United Kingdom Research and Innovation"

class TestConsistency:

    def test_core(self):
        from arraypartition import (
            ArrayLike,
            SuperLazyArrayLike,
            ArrayPartition
        )

        from arraypartition.partition import (
            get_chunk_space,
            get_chunk_shape,
            get_chunk_positions,
            get_chunk_extent,
            get_dask_chunks,
            combine_sliced_dim,
            combine_slices,
            normalize_partition_chunks
        )

        assert True