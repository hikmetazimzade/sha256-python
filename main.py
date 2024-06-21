import processing_blocks

if __name__ == '__main__':
    plain_text = "Hello World"
    process_blocks = processing_blocks.Process_Block(plain_text)
    hash_output = process_blocks.get_hash_output()

    print("Hash Output=", hash_output)