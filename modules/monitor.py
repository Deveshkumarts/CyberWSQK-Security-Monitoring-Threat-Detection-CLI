import psutil

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()

    disk = psutil.disk_usage('/')

    processes = len(psutil.pids())

    boot_time = psutil.boot_time()

    return {
        "cpu": cpu,
        "ram": ram.percent,
        "disk": disk.percent,
        "processes": processes,
        "boot_time": boot_time
    }