import argparse
import time

from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


# Initialize BoardShim object to connect to Muse 2 device.
def getBoardShim():
    params = BrainFlowInputParams()
    params.mac_address = "00:55:da:b5:c9:df"
    boardId = BoardIds.MUSE_2_BOARD
    board = BoardShim(boardId, params)
    return board


def main():
    BoardShim.enable_dev_board_logger()

    board = getBoardShim()

    board.prepare_session()
    input("Press Enter to Start Stream")
    board.start_stream()
    timeStart = time.time()
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    input("Press Enter to Stop Stream")
    timeDelta = time.time() - timeStart
    data = board.get_board_data(timeDelta * 256)  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()

    print(data)
    print(data.shape)

    descriptor = BoardShim.get_board_descr(BoardIds.MUSE_2_BOARD)
    pprint(descriptor)

    plt.plot(data[6], data[1])
    plt.plot(data[6], data[2])
    plt.plot(data[6], data[3])
    plt.plot(data[6], data[4])
    plt.legend(descriptor["eeg_names"].split(","))
    plt.show()
    

if __name__ == "__main__":
    main()