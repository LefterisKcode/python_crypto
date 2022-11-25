from Pyfhel import Pyfhel, PyCtxt, PyPtxt
import pickle

HE = Pyfhel()  # Creating empty Pyfhel object
bfv_params = {
    'scheme': 'BFV',  # can also be 'ckks'
    'n': 2 ** 13,  # Polynomial modulus degree, the num. of slots per plaintext,
    #  of elements to be encoded in a single ciphertext in a
    #  2 by n/2 rectangular matrix (mind this shape for rotations!)
    #  Typ. 2^D for D in [10, 16]
    't': 65537,  # Plaintext modulus. Encrypted operations happen modulo t
    #  Must be prime such that t-1 be divisible by 2^N.
    't_bits': 20,  # Number of bits in t. Used to generate a suitable value
    #  for t. Overrides t if specified.
    'sec': 128,  # Security parameter. The equivalent length of AES key in bits.
    #  Sets the ciphertext modulus q, can be one of {128, 192, 256}
    #  More means more security but also slower computation.
}
print("---------------------------------------------------")

HE.load_context('./context.txt')
HE.load_public_key('./public_k.txt')
HE.load_secret_key('./secret_k.txt')



def serialize_message(message):
    dff = list(message)
    erDf = [ord(n) for n in dff]
    cctxt2 = HE.encrypt(erDf)  # encrypts the plaintext
    return pickle.dumps(cctxt2)

def deserialize_message(message):
    return pickle.loads(message)


if __name__ == '__main__':
    message1 = serialize_message("Hello world")
    message2 = serialize_message("Hello greece")
    parsed_msg = deserialize_message(message1)
    parsed_msg2 = deserialize_message(message2)
    # Here we have a list of encryprted message objects
    messages = [
        parsed_msg,
        parsed_msg2
    ]
    # Here we have encrypted messages as byte strings 
    raw_messages = [
        message1,
        message2
    ]
    dummy_word = "greece"
