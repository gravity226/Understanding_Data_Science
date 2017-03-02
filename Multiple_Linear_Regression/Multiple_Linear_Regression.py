from __future__ import division
import numpy as np

# Multiple Linear Regression formula
# y = B_0 + (B_1 * X_1) + (B_2 * X_2) + ... + (B_n * X_n)
# Betas = np.linalg.inv(X.T * X) * X.T * y


class Multiple_Linear_Regression(object):
    def __init__(self):
        self.X = []
        self.y = []
        self.betas = []

    def fit(self, X, y):
        self.X = np.array([ [1] + list(row) for row in X ])
        self.y = np.array(y)

        if self.X.shape[0] == self.y.shape[0]:
            self.betas = self.get_betas()

        else:
            print "X and y must have the same number of records"

    def get_betas(self):
        return np.linalg.inv( self.X.T.dot(self.X)).dot(self.X.T).dot(self.y)

    def predict(self, X):
        '''
        must be a 2d array, ie X = [[1,2,3],[3,4,5]]
        '''
        X = [ row for row in X ]
        return [ sum([self.betas[0]] + [ val * self.betas[n+1] for n, val in enumerate(row) ]) for row in X ]



if __name__ == '__main__':
    X = [[1, 2, 30, 4], [3, 1, 40, 2], [1, 2, 30, 9], [5, 3, 20, 1], [9, 6, 21, 3]]
    y = [1,2,3,4,5]
    model = Multiple_Linear_Regression()
    model.fit(X, y)
    print model.predict([[1,2,30,4]])




















#
