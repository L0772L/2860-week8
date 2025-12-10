class VigenereCipher:
    """
       VigenereCipher class (TO BE COMPLETED).

       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        """
        Private method to shift a letter a number of positions forward or backward in the alphabet.
        """
        # convert letter to number 0-25
        pos = ord(letter) - self.offset

        # forward: add shift, backward: subtract shift
        if forward:
            new_pos = (pos + shift) % 26
        else:
            new_pos = (pos - shift) % 26

        return chr(self.offset + new_pos)

    def __generate_shift_list(self, plaintext_length: int):
        """
        Repeats the keyword until length matches plaintext_length
        then converts each letter to shift (A=0, ..., Z=25)
        """
        repeats = (plaintext_length // len(self.keyword)) + 1
        repeated_keyword = (self.keyword * repeats)[:plaintext_length]

        # convert each keyword letter to shift amount
        return [ord(ch) - self.offset for ch in repeated_keyword]

    def encrypt(self, plaintext: str):
        """
        Encrypts a plaintext string.
        Steps:
            1. Convert lowercase to uppercase
            2. Remove whitespace and punctuation
            3. Generate shift list
            4. Shift each letter
        """
        cleaned = ''.join([ch.upper() for ch in plaintext if ch.isalpha()])

        shifts = self.__generate_shift_list(len(cleaned))

        ciphertext = ""
        for i, ch in enumerate(cleaned):
            shift = shifts[i]
            cipher_letter = self.__shift_letter(ch, shift, True)
            ciphertext += cipher_letter

        return ciphertext

    def decrypt(self, ciphertext: str):
        """
        Decrypts a ciphertext string (reverse of encrypt)
        """
        cleaned = ''.join([ch.upper() for ch in ciphertext if ch.isalpha()])

        shifts = self.__generate_shift_list(len(cleaned))

        plaintext = ""
        for i, ch in enumerate(cleaned):
            shift = shifts[i]
            plain_letter = self.__shift_letter(ch, shift, False)
            plaintext += plain_letter

        return plaintext


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()

