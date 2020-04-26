import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

class Komparator():

    def __init__(self, df):
        self.df = df

    # displays a series of box plots to compare the distribution of the numerical variable in each possible value of the categorical variable.
    # There should be as many box plots as there are possible values of the categorical variable.
    # For example, with Sex and Height, we would compare the distribution of height between men and women with two box plots.
    def compare_box_plots(self, categorical_var, numerical_var):
        filtred = self.df.drop_duplicates(subset=categorical_var)

        categorical_values = filtred[categorical_var].values.tolist()
        length = len(categorical_values)

        dummy_f, ax = plt.subplots(1, length)
        for i in range(0, length):
            ax[i].set_title('Boxplot for {} with value {}'.format(categorical_var, categorical_values[i]))
            data = self.df[self.df[categorical_var].eq(categorical_values[i])]
            sns.boxplot(data=data[[categorical_var, numerical_var]], ax=ax[i])

        plt.show()


    # displays the density of the numerical variable, with a different curve for the subpopulation which belongs to each categorical variable.
    def density(self, categorical_var, numerical_var):
        filtred = self.df.drop_duplicates(subset=categorical_var)

        categorical_values = filtred[categorical_var].values.tolist()
        length = len(categorical_values)

        dummy_f, ax = plt.subplots(1, length)
        for i in range(0, length):
            ax[i].set_title('Density for {} with value {}'.format(categorical_var, categorical_values[i]))

            data = self.df[self.df[categorical_var].eq(categorical_values[i])]
            data[[categorical_var, numerical_var]].plot.kde(ax=ax[i])

        plt.show()
    
    # displays separate histograms of the numerical variable for each category represented in the categorical variable.
    # As a bonus, you can make it display overlapping histograms of different colors.
    def compare_histograms(self, categorical_var, numerical_var, overlap=False):
        colors=['r', 'g', 'b', 'c']
        filtred = self.df.drop_duplicates(subset=categorical_var)

        categorical_values = filtred[categorical_var].values.tolist()
        length = len(categorical_values)

        if overlap == True:
            axes = None
            for i in range(0, length):
                data = self.df[self.df[categorical_var].eq(categorical_values[i])]

                if axes == None:
                    axes = data[[categorical_var, numerical_var]].hist(alpha=0.5, label=categorical_values[i], color=colors[i%len(colors)])
                else:
                    data[[categorical_var, numerical_var]].hist(ax=axes.ravel()[:length], alpha=0.5, color=colors[i%len(colors)], label=categorical_values[i])
            plt.suptitle('Historigrams for {} with {}'.format(categorical_var, numerical_var))
            plt.legend(prop={'size': 10})
        else:
            dummy_f, ax = plt.subplots(1, length)
            for i in range(0, length):
                ax[i].set_title('Historigrams for {} with value {}'.format(categorical_var, categorical_values[i]))

                data = self.df[self.df[categorical_var].eq(categorical_values[i])]
                data[[categorical_var, numerical_var]].hist(ax=ax[i])

        plt.show()

