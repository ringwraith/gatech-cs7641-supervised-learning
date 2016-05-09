
import matplotlib.pyplot as plt
import pandas as pd
import sys


def load_data(file):
    return pd.read_csv(file, index_col='training_set')


def plot_data(df, title='', xlabel='Training set size', ylabel='Error'):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


if __name__ == "__main__":
    df = load_data('../spectrometer/Boosting_AdaBoostM1/_results.csv')
    print df
    plot_data(df, 'Spectrometer - Boosting (AdaBoostM1)')
