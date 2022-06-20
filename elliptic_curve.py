from ecdsa import SigningKey, SECP256k1

"""
 generate private and public key
"""
private_key = SigningKey.generate(SECP256k1)
public_key = private_key.get_verifying_key()
print(private_key.to_string().hex(), public_key.to_string().hex(), sep="\n\n")


"""
SIGN A AMESSAGE
"""
msg = b"STUFF"
signature = private_key.sign(msg)
print(signature)

"""
VERIFY THE SIGNATURE
"""
print(public_key.verify(signature, msg + b"wrong"))
