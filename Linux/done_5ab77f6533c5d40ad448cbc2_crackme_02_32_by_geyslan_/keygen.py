CYPHER_TEXT = (0xf7, 0xf8, 0xf1, 0xf4, 0xf1, 0xf8, 0xb3, 0xfc, 0xfc, 0x00)
ENCRYPTION_KEY = 0x90
passwd = "".join(chr(i & ~ENCRYPTION_KEY ) for i in CYPHER_TEXT)
print(passwd)