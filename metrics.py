import psutil as p
from sys import argv


def print_cpu_stat():
    print('system.cpu.idle:', p.cpu_times().idle)
    print('system.cpu.user:', p.cpu_times().user)
    print('system.cpu.guest:', p.cpu_times().guest)
    print('system.cpu.iowait:', p.cpu_times().iowait)
    print('system.cpu.stolen:', p.cpu_times().steal)
    print('system.cpu.system:', p.cpu_times().system)


def print_virtual_memory_stat():
    print('virtual total:', p.virtual_memory().total)
    print('virtual used:', p.virtual_memory().used)
    print('virtual free:', p.virtual_memory().free)
    print('virtual shared:', p.virtual_memory().shared)


def print_swap_stat():
    print('swap total:', p.swap_memory().total)
    print('swap used:', p.swap_memory().used)
    print('swap free:', p.swap_memory().free)


if len(argv) > 1:
    if argv[1] == 'cpu':
        print_cpu_stat()
    elif argv[1] == 'mem':
        print_virtual_memory_stat()
        print_swap_stat()
    else:
        print('Not supported option. Please type "cpu" or "mem"')
else:
    print_cpu_stat()
    print_virtual_memory_stat()
    print_swap_stat()

