class Tile:
    is_hidden: bool
    is_mine: bool
    x_coord: int #coordinate within grid of buttons, not on the window
    y_coord: int #coordinate multiplied by a constant to find location
    width: int = 50
    height: int = 50
    adjacent_mines: int
    #reference to pygame button(FUCK YOU)

    def __init__(self, is_hidden, is_mine, x_coord, y_coord, adjacent_mines):
        self.is_hidden = is_hidden
        self.is_mine = is_mine
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.adjacent_mines = adjacent_mines

tile_list: list[list[Tile]] = []

for y in range(25):
    x_list: list[Tile] = []
    for x in range(40):
        x_list.append(Tile(False, False, x, y, 0))
    tile_list.append(x_list)

