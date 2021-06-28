def caesar(text: str, key: int) -> str:
    result: str = ""
    for char in text:
        c: int = ord(char)
        enc_char: str = chr(c + key)
        result += enc_char
    return result

print(caesar("Zakaria Hasan",2))
print(caesar("\cmctkc",-2))
