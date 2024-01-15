import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT


class mainPlot:
    def __init__(self, parent, sub_h=1, sub_v=1) -> None:
        self.fig = plt.figure()  # 新建画板 figure
        self.grid_spec = self.fig.add_gridspec(nrows=sub_h, ncols=sub_v)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar2QT(self.canvas, parent)

        self.clear()

    def set_grid(self, sub_h=1, sub_v=1):
        self.grid_spec = self.fig.add_gridspec(nrows=sub_h, ncols=sub_v)
        return self.grid_spec

    def get_grid(self):
        return self.grid_spec

    def get_axe(
        self, gs_range, gs_h_start=None, gs_h_stop=None, gs_v_start=None, gs_v_stop=None
    ):
        if gs_range:
            return self.fig.add_subplot(gs_range)
        else:
            return self.fig.add_subplot(
                self.grid_spec[gs_h_start:gs_h_stop, gs_v_start, gs_v_stop]
            )

    def get_canvas(self):
        return self.canvas

    def get_toolbar(self):
        return self.toolbar

    def draw(self):
        self.canvas.draw()

    def clear(self):
        self.fig.clear()
        self.draw()


if __name__ == "__main__":
    pass
