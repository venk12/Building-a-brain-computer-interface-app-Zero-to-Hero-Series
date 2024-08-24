import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet, local_clock

# 1. Define constants
SAMPLE_RATE = 250  # Hz
NUM_CHANNELS = 8
STREAM_NAME = "EEG_Simulator"
STREAM_TYPE = "EEG"
CHANNEL_FORMAT = 'float32'

# 2. Create LSL stream info and outlet
info = StreamInfo(name=STREAM_NAME, type=STREAM_TYPE, channel_count=NUM_CHANNELS + 1, nominal_srate=SAMPLE_RATE, channel_format=CHANNEL_FORMAT, source_id="myuid34234")
outlet = StreamOutlet(info)

# 3. Simulate EEG-like data
def generate_eeg_data(num_channels):
    """Simulates EEG data by generating random values similar to real EEG signals."""
    # Typical EEG signal ranges from 0.5 to 100 µV (microvolts) depending on the frequency band
    # We'll generate data around this range.
    return np.random.normal(0, 50, num_channels)  # Gaussian noise with mean=0 and std=50µV

# 4. Start streaming
print("Now sending data...")
start_time = local_clock()
while True:
    # Generate timestamp
    timestamp = local_clock()

    # Generate EEG-like signal values
    eeg_values = generate_eeg_data(NUM_CHANNELS)

    # Combine EEG values with timestamp
    data = np.append(eeg_values, timestamp)

    # Send data via LSL
    outlet.push_sample(data)

    # Wait for the next sample based on the sampling frequency
    time.sleep(1.0 / SAMPLE_RATE)