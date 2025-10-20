enc=b'\x2a\x09\x18\x4b\x08\x18\x4b\x0e\x16\x1f\x04'

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

for a in range(256):
    key=b'ke' + bytes([a])
    print(key,xor(enc,key))

