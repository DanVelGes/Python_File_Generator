import os

def generate_file(file_name, file_size):
    with open(file_name, 'wb') as f:
        f.write(os.urandom(1024 * 1024 * file_size))

# Generate 'test_file.txt' with a size of XXX MB
# XXX for MB, XXXX for GB
generate_file('test_file.txt', 2500)