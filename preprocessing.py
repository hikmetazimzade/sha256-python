class Preprocessing_Algorithm:
    def __init__(self, plain_text):
        self.plain_text = plain_text


    def binary(self, ascii_conversion : int) -> str:
        output = ""
        while ascii_conversion:
            output += str(ascii_conversion % 2)
            ascii_conversion //= 2

        output = output[::-1]
        length = len(output)
        return output if length == 8 else (8 - length) * "0" + output


    def get_binary_len(self, pad_length : int) -> str:
        output = ""
        while pad_length:
            output += str(pad_length % 2)
            pad_length //= 2

        output = output[::-1]
        length = len(output)

        return output if length == 64 else (64 - length) * "0" + output


    def get_padding(self) -> str:
        padded_text = ""

        for p in self.plain_text:
            padded_text += self.binary(ord(p))

        padded_text += "1"
        length = len(padded_text)  # You can use it to see the length of padded text


        while length % 512 != 448:
            padded_text += "0"
            length += 1

        original_length = len(self.plain_text) * 8
        binary_length = self.get_binary_len(original_length)
        padded_text += binary_length

        return padded_text


    def get_parsed_data(self) -> list:
        padded_text = self.get_padding()
        length = len(padded_text)

        parsed_data = []
        for k in range(0, length, 512):
            parsed_data.append(padded_text[k : k + 512])

        return parsed_data