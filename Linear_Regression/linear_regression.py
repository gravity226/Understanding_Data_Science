from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression(object):
    def __init__(self):
        self.X = []
        self.y = []

    def fit(self, X, y):
        if len(X) == len(y):
            self.X = np.array(X)
            self.y = np.array(y)

            self.count = len(X)

            self.x_bar = self.X.mean()
            self.y_bar = self.y.mean()
            self.xy_bar = (self.X * self.y).mean()
            self.x2_bar = (self.X**2).mean()
            self.y2_bar = (self.y**2).mean()

            self.slope = self.get_slope()
            self.y_intercept = self.get_y_intercept()
        else:
            print "X and y must be the same length"

    def get_slope(self):
        return ((self.x_bar * self.y_bar) - self.xy_bar) / (self.x_bar**2 - self.x2_bar)

    def get_y_intercept(self):  # b = y - mx
        return self.y_bar - (self.slope * self.x_bar)

    # How much of the total variation in y is not described by our line of best fit?
    def get_standard_error_line(self):
        return sum([ (y - (self.slope * self.predict_y(x) + self.y_intercept))**2 for x, y in zip(self.X, self.y) ])

    def get_standard_error_y_bar(self):
        return sum([ (y - self.y_bar)**2 for y in self.y ])

    def get_something_error(self):
        return (self.count * self.y2_bar) - \
               (2 * self.slope * self.count * self.xy_bar) - \
               (2 * self.y_intercept * self.count * self.y_bar) + \
               (self.slope ** 2 * self.count * self.x2_bar) + \
               (2 * self.slope * self.y_intercept * self.count * self.x_bar) + \
               (self.count * self.y_intercept**2)

    def predict_y(self, x):
        return self.slope * x + self.y_intercept

    def predict_x(self, y):
        return (y - self.y_intercept) / self.slope

    # How much of the variation in y is described by the variation in x? ref: https://www.youtube.com/watch?v=lng4ZgConCM
    # Coefficient of determination
    # R^2
    def get_r2(self):
        return 1 - (self.get_standard_error_line() / self.get_standard_error_y_bar())

    def get_covariance(self):
        return self.xy_bar - (self.x_bar * self.y_bar)

    def get_variance_x(self):
        return (self.X * self.X).mean() - (self.x_bar * self.x_bar)

    def get_variance_y(self):
        return (self.y * self.y).mean() - (self.y_bar * self.y_bar)

    def plot(self, title="Scatter Plot", save=False, name="Scatter_Plot.png"):
        plt.clf()
        plt.scatter(self.X, self.y)

        x = [ min(self.X), max(self.X) ]
        y = [ self.predict_y(min(self.X)), self.predict_y(max(self.X))]
        plt.plot(x, y, c='r', lw=2)

        plt.title(title)
        plt.show()

        if save:
            plt.savefig(name)


if __name__ == '__main__':
    pass

from Linear_Regression.linear_regression import LinearRegression
lr = LinearRegression()
lr.fit([1,2,3,4,5,6,7,8,9,9], [1,1,3,4,4,5,6,6,7,8])
