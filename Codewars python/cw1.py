def swapAdjacentBits(n):
    # Shift even bits to the right and odd bits to the left, then OR them to combine.
    return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)

