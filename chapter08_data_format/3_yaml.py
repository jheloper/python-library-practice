import yaml

file = open('sample1.yml', 'r')
conf = yaml.load(file)

print(conf)
print(conf['database']['port'])

file.close()

with open('sample2.yml', 'r') as f:
    for data in yaml.load_all(f):
        print(data)

hosts = {'web_server': ['192.169.0.2', '192.168.0.3'], 'db_server': ['192.168.10.7']}

with open('dump.yml', 'w') as f:
    f.write(yaml.dump(hosts, default_flow_style=False))