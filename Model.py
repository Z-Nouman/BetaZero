import tangram
import os
import numpy as np


class Model:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), 'kaggle-set.tangram')
        self.model = tangram.Model.from_path(model_path)
        model_path2 = os.path.join(os.path.dirname(__file__), 'connect4-final-dataset.tangram')
        self.model2 = tangram.Model.from_path(model_path2)
        self.labels = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6',
                       'b1', 'b2', 'b3', 'b4', 'b5', 'b6',
                       'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
                       'd1', 'd2', 'd3', 'd4', 'd5', 'd6',
                       'e1', 'e2', 'e3', 'e4', 'e5', 'e6',
                       'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
                       'g1', 'g2', 'g3', 'g4', 'g5', 'g6', ]

    def predict(self, data):
        sample = dict()
        data = np.flipud(data).ravel(order='F')
        for count, i in enumerate(self.labels):
            sample[i] = data[count]
        return self.model.predict(sample).value

    def predict_early(self, data):
        sample = dict()
        data = np.flipud(data).ravel(order='F')
        for count, i in enumerate(self.labels):
            sample[i] = data[count]
        return self.model2.predict(sample).value
