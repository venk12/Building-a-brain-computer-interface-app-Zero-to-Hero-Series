from pylsl import StreamInlet, resolve_stream

device_name = "<FILL THIS IN>"

signal_stream = resolve_stream('name', device_name)

inlet_signal = StreamInlet(signal_stream[0])

try:
    while True:
        sample, timestamp = inlet_signal.pull_sample()
        # print(sample)

        # If you want to pull as chunk instead
        # sample, timestamp = inlet_signal.pull_chunk()

        if timestamp:
            print("signal stream receiving data...")
            print("Signal Received:\n", sample, "\nSignal Timestamp:", timestamp)


except Exception as e:
    print(f"Signal stream encountered an error: {e}")

finally:
    print("Closing Signal Stream")
    inlet_signal.close_stream()

