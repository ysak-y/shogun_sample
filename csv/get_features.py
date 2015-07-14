# -*- coding: utf-8 -*-

import csv
import numpy as np

if __name__ == "__main__":

    f_name = "feature.csv"

    with open(f_name, "w") as f:

        csv_writer = csv.writer(f)
        for i in range(100):
            arr = np.random.rand(4)
            csv_writer.writerow(arr)

