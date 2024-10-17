
def brute_otp(text):
    for key in range(256):
        #xoram bytes
        dec = "".join([chr(ord(c) ^ key) for c in text])
        print(f"Key: {key} -> Decrypted text: {dec}")

with open("isc-lab02-otp.txt", 'r') as f:
    chestie = f.read()
brute_otp(chestie)
