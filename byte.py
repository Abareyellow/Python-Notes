print(bytes(4))
cookieBytes = bytes('🍪', 'utf-8')
cookieBites = bytearray('🍪', 'utf-8')
print(cookieBites)
cookieBites[3] = int('85', 16)
print(cookieBytes)
print(cookieBites.decode('utf-8'))
print(cookieBytes.decode('utf-8'))