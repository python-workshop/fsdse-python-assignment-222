def calc_utopian_tree_height(cycles):
    height = 1
    if cycles == 0:
        return height
    for i in range(1, cycles+1):
        if i % 2 == 1:
            height *= 2
        else:
            height += 1
    return height

print(calc_utopian_tree_height(0))