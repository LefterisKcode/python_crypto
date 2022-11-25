from pyope.ope import OPE
import numpy as np

random_k = OPE.generate_key()
ptxt = OPE(random_k)

strs = "leftkoutsour@gmail.com"
dummy_s = "leftkoutsour@gmail.com"
y = [ord(x) for x in dummy_s]
f = [ord(x) for x in strs]
enc_arr = [ptxt.encrypt(h) for h in f]
enc_arr2 = [ptxt.encrypt(n) for n in y]
print("Encrypted text 1 --> ",enc_arr)
print("Encrypted text 2 --> ",enc_arr2)
cn = len(enc_arr)
cn2 = len(enc_arr2)
k = 0
cnt = 0
q = 0
i = 0

while k < cn:
    try:
        for i in range(cn2):
            if enc_arr2[i] == enc_arr[i + q] and (cnt != cn2):
                cnt += 1
            else:
                k += 1
                q += 1
                break
        if (cnt == cn2) and (enc_arr2[i] == enc_arr[i + q]):
            print("\n\n <<<< Match found successfully! >>>>")
            break
    except:
        print()

if k == cn:
    print("\n\n <<<< Sorry! No match found.. >>>>")