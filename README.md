# Muse 2 Notes
## Brainflow Library

Brainflow is a library for connecting to Muse 2 devices. 
This is a minimal example of connecting to a Muse 2 device using python version of Brainflow.

```python
# Initializing device object
BoardShim.enable_dev_board_logger()
params = BrainFlowInputParams()
params.mac_address = "<mac address of device>"
board = BoardShim(BoardIds.MUSE_2_BOARD, params)

# Start collecting data
board.prepare_session()
board.start_stream()
time.sleep(1)
data = board.get_board_data(100)
board.stop_stream()
board.release_session()

# Output data
print(data)
```

The format of the Muse 2 data is described by `BoardShim.get_board_descr(BoardIds.MUSE_2_BOARD)`. Attributes named as `x_channels` describes the data in those row indices. 
```
{'eeg_channels': [1, 2, 3, 4],
 'eeg_names': 'TP9,Fp1,Fp2,TP10',
 'marker_channel': 7,
 'name': 'Muse2',
 'num_rows': 8,
 'other_channels': [5],
 'package_num_channel': 0,
 'sampling_rate': 256,
 'timestamp_channel': 6}
```

To get the data from different sensors (EEG, PPG, and Gyroscope). The default value for `get_board_data()` is `BrainFlow.DEFAULT_PRESET`.
```python
data_default = BrainFlow.get_board_data(board_shim, BrainFlow.DEFAULT_PRESET) # contains eeg data
data_aux = BrainFlow.get_board_data(board_shim, BrainFlow.AUXILIARY_PRESET) # contains accel and gyro data
data_anc = BrainFlow.get_board_data(board_shim, BrainFlow.ANCILLARY_PRESET) # contains ppg data
```