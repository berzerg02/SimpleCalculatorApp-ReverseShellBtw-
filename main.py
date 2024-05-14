import os
import random
import secrets

def generate_random_hex(length):
    return ''.join(secrets.choice('0123456789ABCDEF') for _ in range(length))

def generate_dummy_dll(size):
    # Magic number for DLL files
    magic_number = b'\x4D\x5A'  # "MZ"

    # Placeholder for the rest of the DLL content
    rest_of_dll = bytearray(size - len(magic_number))
    rest_of_dll[:] = [random.randint(0, 255) for _ in range(size - len(magic_number))]

    return magic_number + rest_of_dll

# Usage example
if __name__ == "__main__":
    dll_count = 20  # Number of dummy DLLs to generate
    min_size = 1024  # Minimum size of each dummy DLL (in bytes)
    max_size = 4096  # Maximum size of each dummy DLL (in bytes)
    output_path = input("Enter the path where you want to generate the files: ").strip()

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for i in range(dll_count):
        size = random.randint(min_size, max_size)  # Random size for each DLL
        filename = os.path.join(output_path, generate_random_hex(8) + ".dll")  # Generating a random hexadecimal name
        dll_data = generate_dummy_dll(size)
        with open(filename, 'wb') as f:
            f.write(dll_data)
        print(f"Dummy DLL file '{filename}' generated successfully.")
