class Piece:
    def __init__(self, piece_value):
        if piece_value == None or piece_value < 0 or 16 <= piece_value:  # empty piece case
            self._value = -1
            self._bin_value = None
            return

        self._value = piece_value

        self._bin_value = [0, 0, 0, 0]
        if piece_value >= 8:  # color
            self._bin_value[0] = 1
            piece_value -= 8
        if piece_value >= 4:  # shape
            self._bin_value[1] = 1
            piece_value -= 4
        if piece_value >= 2:  # filling
            self._bin_value[2] = 1
            piece_value -= 2
        self._bin_value[3] = piece_value  # height

    def is_idle(self):
        return self._bin_value == None

    def is_white(self):
        return self._bin_value[0] == 1

    def is_circle(self):
        return self._bin_value[1] == 1

    def is_filled(self):
        return self._bin_value[2] == 1

    def is_high(self):
        return self._bin_value[3] == 1

    def decimal(self):  # empty pieces return -1
        return self._value

    def binary(self):  # empty pieces return None
        return self._bin_value

    def __str__(self):
        return f"{self._bin_value[0]}{self._bin_value[1]}\n{self._bin_value[2]}{self._bin_value[3]}"
