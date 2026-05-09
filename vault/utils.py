import base64

def get_part_2():
    return base64.b64decode("Y2h0b195YV8=").decode()

def get_part_3():
    xor_key = 42
    cipher_data = [80, 68, 75, 70, 117, 69, 117] 
    return "".join([chr(b ^ xor_key) for b in cipher_data])
