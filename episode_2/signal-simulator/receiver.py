from pylsl import StreamInlet, resolve_stream

# 1. Resolve the stream
print("Looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# 2. Create an inlet to read from the stream
inlet = StreamInlet(streams[0])

print("Connected to stream. Now receiving data...")

while True:
    # 3. Get a new sample (signal values + timestamp)
    sample, timestamp = inlet.pull_sample()
    
    # 4. Print the received data to console
    signal_values = sample[:-1]
    received_timestamp = sample[-1]
    
    print(f"Received at {received_timestamp:.5f}: {signal_values}")