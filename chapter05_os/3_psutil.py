import psutil

print(psutil.cpu_count())

print(psutil.disk_partitions())
print(psutil.disk_usage('/'))

print(psutil.net_connections())
print(psutil.net_if_stats())

for i in range(5):
    print(psutil.cpu_percent(interval=1, percpu=True))
    print(psutil.virtual_memory())
    print(psutil.swap_memory())
    print(psutil.disk_io_counters(perdisk=False))
    print(psutil.net_io_counters())
