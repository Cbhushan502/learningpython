import re

def parse_task_data(task_data):
    lines = task_data.strip().split('\n')
    headers = re.split(r'\s+', lines[0].strip())
    processes = []

    for line in lines[1:]:
        values = re.split(r'\s+', line.strip())
        process = {}
        for i, value in enumerate(values):
            header = headers[i]
            if value == 'null':
                process[header] = None
            elif header in ['PID', 'NI']:
                process[header] = int(value)
            elif header in ['%CPU', '%MEM']:
                process[header] = float(value)
            else:
                process[header] = value
        processes.append(process)

    return processes