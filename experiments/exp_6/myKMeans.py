import numpy as np


# sample: (x, y), samples: list[sample]
class MyKMeans:
    def __init__(self) -> None:
        self.centers = {}

    def add_center(self, samples, key):
        x_center = np.mean([i[0] for i in samples])
        y_center = np.mean([i[1] for i in samples])
        self.centers[(x_center, y_center)] = key
        return (x_center, y_center)

    def find_nearest_center(self, sample):
        x_sample, y_sample = sample

        min_distance = np.inf
        nearest_center = None
        for center in self.centers.keys():
            x_center, y_center = center
            distance = (x_center - x_sample) ** 2 + (y_center - y_sample) ** 2
            if distance < min_distance:
                min_distance = distance
                nearest_center = center
        return self.centers[nearest_center]


if __name__ == "__main__":
    km = MyKMeans()
    km.add_center([(1, 2), (1, 1), (1, 3)], 1)
    km.add_center([(3, 2), (2, 1), (2.5, 2)], 2)
    print(km.centers)
    print(km.find_nearest_center((1, 1)))