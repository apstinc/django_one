import os
import sys
import re
import time
import ctypes
import subprocess

try:
    from django import *
except ImportError:
    subprocess.run(['python', '-m', 'conda', 'install', '--upgrade', 'django'])
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'django'])
    from django import *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                    

# ===============================================================================
#                               Definitions
# ===============================================================================

def run():
    
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    error_file_path = 'error.txt'
    
    # Inintialize
    open(output_file_path, 'w').close()
    open(error_file_path, 'w').close()

    try:
        input_lst = [x.strip() for x in open(input_file_path).read().splitlines()]
    except UnicodeDecodeError:
        try:
            input_lst = [x.strip() for x in open(input_file_path, encoding='cp949').read().splitlines()]
        except UnicodeDecodeError:
            input_lst = [x.strip() for x in open(input_file_path, encoding='utf-8').read().splitlines()]
    
    total_cnt = len(input_lst)

    # TODO: 기능구현

# ===============================================================================
#                            Program infomation
# ===============================================================================

__author__ = '김홍연'
__requester__ = '요청자'
__registration_date__ = '230302'
__latest_update_date__ = '230302'
__version__ = 'v1.00'
__title__ = 'django_one'
__desc__ = 'django_one'
__changeLog__ = {
    'v1.00': ['Initial Release.'],
}
version_lst = list(__changeLog__.keys())

full_version_log = '\n'
short_version_log = '\n'

for ver in __changeLog__:
    full_version_log += f'{ver}\n' + '\n'.join(['    - ' + x for x in __changeLog__[ver]]) + '\n'

if len(version_lst) > 5:
    short_version_log += '.\n.\n.\n'
    short_version_log += f'{version_lst[-2]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-2]]]) + '\n'
    short_version_log += f'{version_lst[-1]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-1]]]) + '\n'

# ===============================================================================
#                                 Main Code
# ===============================================================================

if __name__ == '__main__':

    ctypes.windll.kernel32.SetConsoleTitleW(f'{__title__} {__version__} ({__latest_update_date__})')

    sys.stdout.write(f'{__title__} {__version__} ({__latest_update_date__})\n')

    sys.stdout.write(f'{short_version_log if short_version_log.strip() else full_version_log}\n')

    run()