def decoder(txt, shift):
    res = ""
    for char in txt:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            res += chr((ord(char) - base - shift) % 26 + base)
        else:
            res += char
    return res


encoded = "cdiiddwpgswtgt"

for shift in range(26):
    decoded = decoder(encoded, shift)
    print(f"ROT {shift}: {decoded}")
