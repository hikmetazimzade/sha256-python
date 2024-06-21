import constants
import preprocessing
from extending_blocks import Extend_Class


class Process_Block:
    def __init__(self, plain_text : str):
        preprocess = preprocessing.Preprocessing_Algorithm(plain_text)
        parsed_data = preprocess.get_parsed_data()

        extend_blocks = Extend_Class(parsed_data)
        self.extended_data = extend_blocks.get_extended_data()


    def compression_loop(self, a : int, b : int, c : int, d : int,
                         e : int, f : int, g : int, h : int, W : list, K : list) -> tuple:
        def Ch(x, y, z):
            return (x & y) ^ ((~x) & z)

        def Maj(x, y, z):
            return (x & y) ^ (x & z) ^ (y & z)

        def Sigma0(x):
            return Extend_Class.right_rotate(x, 2) ^ Extend_Class.right_rotate(x, 13) ^ Extend_Class.right_rotate(x, 22)

        def Sigma1(x):
            return Extend_Class.right_rotate(x, 6) ^ Extend_Class.right_rotate(x, 11) ^ Extend_Class.right_rotate(x, 25)

        for i in range(64):
            T1 = (h + Sigma1(e) + Ch(e, f, g) + K[i] + W[i]) & 0xFFFFFFFF
            T2 = (Sigma0(a) + Maj(a, b, c)) & 0xFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + T1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xFFFFFFFF

        return a, b, c, d, e, f, g, h


    def get_hash_output(self) -> str:
        extended_data = self.extended_data
        K = constants.get_constants()
        h0, h1, h2, h3, h4, h5, h6, h7 = constants.initial_values()

        for k in extended_data:
            a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7
            a, b, c, d, e, f, g, h = self.compression_loop(a, b, c, d, e, f, g, h, k, K)

            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF

            h4 = (h4 + e) & 0xFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFF

        return ''.join(f"{x:08x}" for x in [h0, h1, h2, h3, h4, h5, h6, h7])