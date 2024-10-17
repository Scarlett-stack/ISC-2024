import base64

# You are given a string that has been encoded multiple times.
# Your goal is to repeatedly decode it until you reveal the hidden flag.
# You do not know how many times the text has been encoded.

encoded_text = b'VmxSR1lWUXhTa2hXYWxwV1ZrVkthRlpyVm1GamJHUlhWV3RhVG1FemFGWldWbWhyVjJ4YVNGUnFRbFZoTVVwVFdsZHpOVlpGTVZoaVJuQlhUVVJGZWxaRldtdFVNa3BIWWtoR1YySlhlRTlaVjNSTFlqRmtjMVZzU2s5U1ZFWmFWRlZSZDFCUlBUMD0='
decoded_text = base64.b64decode(encoded_text)
decoded_text = base64.b64decode(decoded_text)
decoded_text = base64.b64decode(decoded_text)
decoded_text = base64.b64decode(decoded_text)
decoded_text = base64.b64decode(decoded_text)
#decoded_text = base64.b64decode(decoded_text)
# TODO 1: Decode the string repeatedly until the text is not encoded anymore

print("Final decoded text:", decoded_text)
