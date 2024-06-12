def binary_to_hex(file_path):
    with open(file_path, 'rb') as f:
        binary_data = f.read()
    # convert payload binary to hex
    hex_data = ', '.join(f'0x{byte:02x}' for byte in binary_data)
    return hex_data

# make sure binary file is in current directory
file_path = './payload.bin'

hex_value = binary_to_hex(file_path)
print("Output:\n", hex_value)