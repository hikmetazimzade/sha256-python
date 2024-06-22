# SHA-256 Implementation in Python

This repository contains a Python implementation of the SHA-256 cryptographic hash function. SHA-256 is part of the SHA-2 family, widely used in various security protocols and applications for ensuring data integrity and security.

## Features

- **Pure Python**: The implementation is written entirely in Python.
- **Educational**: Provides a clear, step-by-step explanation of the SHA-256 algorithm.
- **Reusable**: Can be easily integrated into other Python projects.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/hikmetazimzade/SHA256-Python.git
    cd SHA256-Python
    ```

2. **Install dependencies**

    There are no external dependencies required for this implementation.



### Example

Here is a simple example to demonstrate the usage:

```python
import processing_blocks

if __name__ == '__main__':
    plain_text = "Hello World"
    process_blocks = processing_blocks.Process_Block(plain_text)
    hash_output = process_blocks.get_hash_output()

    print("Hash Output=", hash_output)
