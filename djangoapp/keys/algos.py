PUBLICKEY_ALGORITHMS = {
    1: "RSA (Encrypt or Sign)",
    2: "RSA Encrypt-Only",
    3: "RSA Sign-Only",
    16: "Elgamal (Encrypt-Only)",
    17: "DSA (Digital Signature Algorithm)",
    18: "ECDH public key algorithm",
    19: "ECDSA public key algorithm",
    20: "Reserved (formerly Elgamal Encrypt or Sign)",
    21: "Reserved for Diffie-Hellman (X9.42, as defined for IETF-S/MIME)",
    22: "EdDSA public key algorithm",
    100: "Private or experimental",
    101: "Private or experimental",
    102: "Private or experimental",
    103: "Private or experimental",
    104: "Private or experimental",
    105: "Private or experimental",
    106: "Private or experimental",
    107: "Private or experimental",
    108: "Private or experimental",
    109: "Private or experimental",
    110: "Private or experimental",
}

SYMMETRICKEY_ALGORITHMS = {
    0: "Plaintext or unencrypted data",
    1: "IDEA",
    2: "TripleDES",
    3: "CAST5",
    4: "Blowfish",
    5: "Reserved",
    6: "Reserved",
    7: "AES with 128-bit key",
    8: "AES with 192-bit key",
    9: "AES with 256-bit key",
    10: "Twofish with 256-bit key",
    100: "Private or experimental",
    101: "Private or experimental",
    102: "Private or experimental",
    103: "Private or experimental",
    104: "Private or experimental",
    105: "Private or experimental",
    106: "Private or experimental",
    107: "Private or experimental",
    108: "Private or experimental",
    109: "Private or experimental",
    110: "Private or experimental",
}

COMPRESSION_ALGORITHMS = {
    0: "Uncompressed",
    1: "ZIP",
    2: "ZLIB",
    3: "BZip2",
    100: "Private or experimental",
    101: "Private or experimental",
    102: "Private or experimental",
    103: "Private or experimental",
    104: "Private or experimental",
    105: "Private or experimental",
    106: "Private or experimental",
    107: "Private or experimental",
    108: "Private or experimental",
    109: "Private or experimental",
    110: "Private or experimental",
}

HASH_ALGORITHMS = {
    1: "MD5",
    2: "SHA1",
    3: "RIPEMD160",
    4: "Reserved",
    5: "Reserved",
    6: "Reserved",
    7: "Reserved",
    8: "SHA256",
    9: "SHA384",
    10: "SHA512",
    11: "SHA224",
    100: "Private or experimental",
    101: "Private or experimental",
    102: "Private or experimental",
    103: "Private or experimental",
    104: "Private or experimental",
    105: "Private or experimental",
    106: "Private or experimental",
    107: "Private or experimental",
    108: "Private or experimental",
    109: "Private or experimental",
    110: "Private or experimental",
}

ECC_CURVES = {
    "2a8648ce3d030107":   "NIST curve P-256",
    "2b81040022":         "NIST curve P-384",
    "2b81040023":         "NIST curve P-521",
    "2b8104000a":         "secp256k1",
    "2b2403030208010107": "brainpoolP256r1",
    "2b240303020801010b": "brainpoolP384r1",
    "2b240303020801010d": "brainpoolP512r1",
}
