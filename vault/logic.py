def get_part_5():
    cipher = "wqzmgl_vgl_bz}"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    atbash_map = str.maketrans(alphabet, alphabet[::-1])
    return cipher.translate(atbash_map)
