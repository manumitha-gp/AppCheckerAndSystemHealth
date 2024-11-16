import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory Usage: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space: {disk_usage}%")
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    return process_count

if __name__ == "__main__":
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_usage()
    processes = check_running_processes()

    logging.info(f"CPU Usage: {cpu}%")
    logging.info(f"Memory Usage: {memory}%")
    logging.info(f"Disk Usage: {disk}%")
    logging.info(f"Running Processes: {processes}")
    print("System health check complete. Check 'system_health.log' for details.")


