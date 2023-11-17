import argparse
import time

from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from muse import Muse, Data


def plotData(eegData):
    data = eegData.getAllData()
    plt.plot(data[0], data[2])
    plt.plot(data[0], data[3])
    plt.plot(data[0], data[4])
    plt.plot(data[0], data[5])
    plt.legend(Muse.EEG_NAMES)
    plt.show()


def main():
    BoardShim.enable_dev_board_logger()

    muse = Muse("00:55:da:b5:c9:df")
    eegData = muse.sampleData(samplingTime=5)

    print(eegData.getAllData())
    plotData(eegData)
    

if __name__ == "__main__":
    main()
