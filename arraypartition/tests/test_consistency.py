class TestConsistency:

    def test_core(self):
        from ArrayPartition import (
            ArrayLike,
            SuperLazyArrayLike,
            ArrayPartition,
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