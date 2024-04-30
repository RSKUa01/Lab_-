import numpy as np

class LSFR:
    def __init__(self, seed):
        self.state = seed

    def shift(self):
        xor_result = (self.state >> 0) ^ (self.state >> 2) ^ (self.state >> 3) ^ (self.state >> 5)
        self.state = (self.state >> 1) | ((xor_result & 1) << 7)
        return self.state

def encrypt_image(original_image, seed):
    lsfr = LSFR(seed)
    
    # Define the dimension of the puzzle
    rows = 4
    cols = 3

    # Split the original image into puzzle pieces
    pieces = np.array_split(original_image, rows * cols)

    # Create a permutation table using LSFR
    permutation_table = [lsfr.shift() for _ in range(rows * cols)]

    # Rearrange the puzzle pieces based on the permutation table
    rearranged_pieces = [pieces[i] for i in permutation_table]

    # Concatenate the rearranged pieces to form the scrambled image
    scrambled_image = np.concatenate(rearranged_pieces)

    return scrambled_image

def decrypt_image(encrypted_image, seed):
    lsfr = LSFR(seed)

    # Define the dimension of the puzzle
    rows = 4
    cols = 3

    # Split the scrambled image into puzzle pieces
    pieces = np.array_split(encrypted_image, rows * cols)

    # Create a permutation table using LSFR (same as encryption)
    permutation_table = [lsfr.shift() for _ in range(rows * cols)]

    # Reconstruct the original permutation table by reversing the permutation
    inverse_permutation_table = [permutation_table.index(i) for i in range(rows * cols)]

    # Rearrange the puzzle pieces based on the inverse permutation table
    rearranged_pieces = [pieces[i] for i in inverse_permutation_table]

    # Concatenate the rearranged pieces to form the original image
    original_image = np.concatenate(rearranged_pieces)

    return original_image

# Example usage
decrypted_image = decrypt_image(encrypted_image, seed)
