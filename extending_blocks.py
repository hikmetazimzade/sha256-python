class Extend_Class:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data

    @staticmethod
    def right_rotate(value : int, bits : int) -> int:
        """Perform right rotation of a 32-bit integer."""
        return ((value >> bits) | (value << (32 - bits))) & 0xFFFFFFFF

    @staticmethod
    def sigma0(x : int) -> int:
        """SHA-256 σ0 function."""
        return Extend_Class.right_rotate(x, 7) ^ Extend_Class.right_rotate(x, 18) ^ (x >> 3)

    @staticmethod
    def sigma1(x : int) -> int:
        """SHA-256 σ1 function."""
        return Extend_Class.right_rotate(x, 17) ^ Extend_Class.right_rotate(x, 19) ^ (x >> 10)


    def get_separated_parts(self, parsed_data : list) -> list:
        separated_parts = []
        for p in parsed_data:
            separated_parts.append([p[k : k + 32] for k in range(0, 512, 32)])

        return separated_parts



    def extend_function(self, W : list) -> list:
        for i in range(16, 64):
            s0 = self.sigma0(W[i - 15])
            s1 = self.sigma1(W[i - 2])
            W.append((W[i - 16] + s0 + W[i - 7] + s1) & 0xFFFFFFFF)

        return W


    def get_extended_data(self) -> list:
        parsed_data = self.parsed_data
        separated_parts = self.get_separated_parts(parsed_data)
        int_representation = [[int(b, 2) for b in s] for s in separated_parts]

        output = []
        for i in int_representation:
            extended_text = self.extend_function(i)
            output.append(extended_text)

        return output