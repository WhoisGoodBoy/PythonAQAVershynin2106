import subprocess
import time
import concurrent.futures
import datetime


'''print(datetime.datetime.now())
result = subprocess.run(['python', 'threads_example.py'], shell=True, capture_output=True, text=True)
print(result.stdout)
print(datetime.datetime.now())
print('we`re gonna try call func')
subprocess.call(['python', 'threads_example.py'],shell=True, text=True)
print(datetime.datetime.now())
'''

def threads_subprocess(name):
    print(f'we`re in {name} file')
    result = subprocess.run(['python', name], shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(f'we`re exited {name} file')


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(threads_subprocess, ['threads_example.py', 'threads_example2.py'])
