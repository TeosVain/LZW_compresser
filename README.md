# LZW Text Compression Tool

A Python implementation of LZW (Lempel-Ziv-Welch) algorithm for compressing and decompressing text data.

## Features
- Compresses text using **LZW algorithm** with fixed dictionary size
- Supports **English letters**, spaces, and basic punctuation (`. , ! ? -`)
- Encodes data into **bytes** (0-255) for compact storage
- Simple command-line interface

## Usage

### Compression
1. Run with command `pack`
2. Enter text to compress (letters + supported punctuation)
3. Get **byte count** and **byte sequence**

Example:
```
pack
hello world
23
104 101 108 108 111 32 119 111 114 108 100
```

### Decompression
1. Run with command `unpack`
2. Enter byte count and space-separated bytes
3. Get original text

Example:
```
unpack
23
104 101 108 108 111 32 119 111 114 108 100
hello world
```

## Technical Details
- **Dictionary size**: Fixed at 2¹¹ entries (2048)
- **Bit allocation**:
  - 11 bits for phrase codes
  - 5 bits for character encoding
- **Byte packing**: Each code pair (phrase + char) packed into 2 bytes

## Limitations
- Maximum dictionary size fixed at 2048 entries
- Supports only specified characters in `ALPHABET`
- Not optimized for very large texts

## Dependencies
- Python 3.x
- No external libraries required
