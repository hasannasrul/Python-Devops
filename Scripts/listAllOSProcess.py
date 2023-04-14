import psutil

# Get the list of all processes
all_processes = psutil.process_iter()

# Initialize empty lists for running, stopped, and zombie processes
running_processes = []
stopped_processes = []
zombie_processes = []

# Iterate through each process and add it to the appropriate list
for process in all_processes:
    status = process.status()
    if status == psutil.STATUS_RUNNING:
        running_processes.append(process)
    elif status == psutil.STATUS_STOPPED:
        stopped_processes.append(process)
    elif status == psutil.STATUS_ZOMBIE:
        zombie_processes.append(process)

# Print the list of running processes
print("Running Processes:")
for process in running_processes:
    print("  PID={}, Name={}".format(process.pid, process.name()))

# Print the list of stopped processes
print("Stopped Processes:")
for process in stopped_processes:
    print("  PID={}, Name={}".format(process.pid, process.name()))

# Print the list of zombie processes
print("Zombie Processes:")
for process in zombie_processes:
    print("  PID={}, Name={}".format(process.pid, process.name()))
