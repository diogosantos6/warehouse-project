import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()
        # TODO
        self.line_forklift = 0
        self.column_forklift = 0

        self.rows = rows
        self.columns = columns
        self.matrix = matrix

        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = matrix[i][j]
                if self.matrix[i][j] == constants.FORKLIFT:
                    self.line_forklift = i
                    self.column_forklift = j
                if self.matrix[i][j] == constants.EXIT:
                    self.line_exit = i
                    self.column_exit = j

    def can_move_up(self) -> bool:
        # TODO
        return self.line_forklift != 0 \
            and self.matrix[self.line_forklift - 1][self.column_forklift] != constants.SHELF \
            and self.matrix[self.line_forklift - 1][self.column_forklift] != constants.PRODUCT

    def can_move_right(self) -> bool:
        # TODO
        return self.column_forklift != self.columns - 1 \
            and self.matrix[self.line_forklift][self.column_forklift + 1] != constants.SHELF \
            and self.matrix[self.line_forklift][self.column_forklift + 1] != constants.PRODUCT

    def can_move_down(self) -> bool:
        # TODO
        return self.line_forklift != self.rows - 1 \
            and self.matrix[self.line_forklift + 1][self.column_forklift] != constants.SHELF \
            and self.matrix[self.line_forklift + 1][self.column_forklift] != constants.PRODUCT

    def can_move_left(self) -> bool:
        # TODO
        return self.column_forklift != 0 \
            and self.matrix[self.line_forklift][self.column_forklift - 1] != constants.SHELF \
            and self.matrix[self.line_forklift][self.column_forklift - 1] != constants.PRODUCT

    def move_up(self) -> None:
        # TODO
        self.line_forklift -= 1

    def move_right(self) -> None:
        # TODO
        self.column_forklift += 1

    def move_down(self) -> None:
        # TODO
        self.line_forklift += 1

    def move_left(self) -> None:
        # TODO
        self.column_forklift -= 1

    def get_cell_color(self, row: int, column: int) -> Color:
        if self.matrix[row][column] == constants.EXIT:
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return self.line_forklift == other.line_forklift and self.column_forklift == other.column_forklift
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
