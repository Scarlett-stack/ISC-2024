


mes1 = b"FIRE_NUKES_MELA!"
mes2 = b"SEND_NUDES_MELA!"

def xor_1(arg1, arg2):
    return bytes([b1 ^ b2 for b1, b2 in zip(arg1, arg2)])
xor_dif = xor_1(mes1, mes2)

original_iv = bytes.fromhex("7ec00bc6fd663984c1b6c6fd95ceeef1")
new_iv = xor_1(original_iv, xor_dif)
new_iv_hex = new_iv.hex()
print(new_iv_hex)

