from keygen import KeyGenerator

class EncodeDecoder:
    def __init__(self, kg: KeyGenerator) -> None:
        self.key_generator = kg
    
    def encode(self, message: str) -> str:
        key = self.key_generator.generate_key(len(message))

        encoded_msg = ""
        for i, m in enumerate(message):
            nm = ord(m) - ord('A') + 1
            nk = ord(key[i]) - ord('A') + 1
            ne = nm + nk
            if ne > 26:
                ne -= 26
            encoded_msg+=chr(ne + ord('A') - 1)

        return encoded_msg
    
    def decode(self, message: str) -> str:
        key = self.key_generator.generate_key(len(message))
        decoded_msg = ""
        for i, m in enumerate(message):
            nm = ord(m) - ord('A') + 1
            nk = ord(key[i]) - ord('A') + 1
            ne = nm - nk
            if ne < 0:
                ne += 26
            decoded_msg+=chr(ne + ord('A') - 1)

        return decoded_msg