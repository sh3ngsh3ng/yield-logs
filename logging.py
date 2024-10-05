
import os
import random
import time
import threading

file_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(file_dir, "server.log")

# Function to write logs
def write_log_file(filepath):
    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    log_messages = [
        "Invalid password",
        "Invalid username",
        "Database connection error",
        "Database connection established",
        "User logged in",
        "File not found",
        "Memory usage high"
    ]

    # open log file
    with open(filepath, "a") as file:
        while True:
            log_level = random.choice(log_levels)
            log_message = random.choice(log_messages)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S') # localtime() used if not specified in second argument
            log_entry = f"{timestamp} - {log_level} - {log_message}\n"
            file.write(log_entry)
            file.flush()
            time.sleep(1)

# write_log_file(log_file_path)

# Writing in a separate thread
log_writer_thread = threading.Thread(target=write_log_file, args=(log_file_path,)) # args is tuple
log_writer_thread.daemon = True
log_writer_thread.start()


# Function to read logs
def read_log_file(filepath):
    with open(filepath, "r") as file:
        # move pointer to end of file
        file.seek(0, 2)
        while True:
            line = file.readline() # file pointers move after every readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

# main function call
def monitor_log(filepath):
    log_lines = read_log_file(filepath) # generator function giving a generator object
    for line in log_lines: # for loop halts until new value added into generator object - iterable
        print(f"New log entry: {line.strip()}")


if __name__ == "__main__":
    monitor_log(log_file_path)