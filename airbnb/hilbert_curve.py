def hilbert_curve(x, y, iter):
    if x == 0 and y == 0:
        return 1

    tile_a = 2 ** (iter - 1)
    tile_sz = tile_a ** 2
    pos_x, next_x = divmod(x, tile_a)
    pos_y, next_y = divmod(y, tile_a)

    if pos_x == 0 and pos_y == 1:
        return tile_sz + hilbert_curve(next_x, next_y, iter - 1)
    elif pos_x == 1 and pos_y == 1:
        return tile_sz * 2 + hilbert_curve(next_x, next_y, iter - 1)
    elif pos_x == 0 and pos_y == 0:
        return hilbert_curve(tile_a - 1 - next_y, next_x, iter - 1)
    else:
        return tile_sz * 3 + hilbert_curve(tile_a - 1 - next_y, tile_a - 1 - next_x, iter - 1)


assert hilbert_curve(0, 0, 1) == 1
assert hilbert_curve(0, 0, 2) == 1
assert hilbert_curve(1, 1, 1) == 3
assert hilbert_curve(2, 2, 2) == 9
assert hilbert_curve(3, 0, 2) == 16