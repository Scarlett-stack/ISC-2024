from Cryptodome.Cipher import AES
BLOCK_SIZE = 32
PADDING = b'#'
iv = b"\x00" * 16

def decrypt(enc_text, key):
    aes = AES.new(key,AES.MODE_CBC, iv)
    decript = aes.decrypt(enc_text)
    return decript

def unpad(text):
    return text.rstrip(PADDING) #functie noua nu stiam de ea!

with open('isc-lab02-secret.enc', 'rb') as f:
    key = f.read(BLOCK_SIZE)
    criptat = f.read()

decriptat = decrypt(unpad(criptat),key)

with open('res.jpg', 'wb') as f:
    f.write(decriptat)