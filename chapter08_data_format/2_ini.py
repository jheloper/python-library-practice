from configparser import ConfigParser

config = ConfigParser()
print(config.read('config.ini'))

print(config.sections())

print(config.options('USER_A'))

print('USER_B' in config)

print(config.get('USER_A', 'group'))

print(config.get('USER_A', 'limit'))


