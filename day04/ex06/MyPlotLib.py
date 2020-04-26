import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

class MyPlotLib():

    # plots one histogram for each numerical feature in the list
    def histogram(self, data, features):
        data[features].hist()
        plt.show()

    # plots the density curve of each numerical feature in the list
    def density(self, data, features):
        data[features].plot.kde()
        plt.show()

    # plots a matrix of subplots (also called scatter plot matrix).
    # On each subplot shows a scatter plot of one numerical variable against another one.
    # The main diagonal of this matrix shows simple histograms.
    def pair_plot(self, data, features):
        sns.pairplot(data[features], height=3, plot_kws=dict(linewidth=0), markers=".")
        plt.show()

    # displays a box plot for each numerical variable in the dataset.
    def box_plot(self, data, features):
        sns.boxplot(data=data[features])
        plt.show()
