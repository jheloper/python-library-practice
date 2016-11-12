import email
import email.parser

e_parser = email.parser.Parser()

with open('email.txt') as f:
    m = e_parser.parse(f)
    print(type(m))
    print(m.items())

with open('email.txt') as f:
    s = f.read()
    m = email.message_from_string(s)
    print(m.items())

f = open('email.txt')
msg = email.message_from_file(f)
print(type(msg))

print(msg.is_multipart())

print(msg.get_payload())

print(msg.keys())

print(msg.get('From'))

print(msg.as_string())
