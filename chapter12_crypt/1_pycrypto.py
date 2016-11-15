from Crypto.Hash import MD5, SHA512
from Crypto.PublicKey import RSA
from Crypto import Random

hash_md5 = MD5.new()
hash_md5.update(b'hamegg')
print(hash_md5.hexdigest())

hash_sha512 = SHA512.new()
hash_sha512.update(b'ham')
print(hash_sha512.hexdigest())

hash2_md5 = MD5.new(b'hamegg')
print(hash2_md5.hexdigest())

hash2_sha512 = SHA512.new(b'ham')
print(hash2_sha512.hexdigest())

rsa = RSA.generate(2048)
private_pem = rsa.exportKey(format='PEM', passphrase='password')
with open('private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('public.pem', 'wb') as f:
    f.write(public_pem)

public_key_file = open('public.pem', 'r')
private_key_file = open('private.pem', 'r')

public_key = RSA.importKey(public_key_file.read())
private_key = RSA.importKey(private_key_file.read(), passphrase='password')

plain_text = 'ham'
print('원래 문자열:', plain_text)

random_func = Random.new().read
encrypted = public_key.encrypt(plain_text.encode('utf8'), random_func)
print('암호화된 문자열:', encrypted)

decrypted = private_key.decrypt(encrypted)
print('복호화된 문자열:', decrypted.decode('utf8'))

public_key_file.close()
private_key_file.close()
