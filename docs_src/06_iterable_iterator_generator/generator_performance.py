

# Performance comparison
# I adapte the code from https://github.com/CoreyMSchafer/code_snippets/tree/master/Generators
# to compare the performance of list and generator
# I also fixed some outdated code.

import random
import time
import psutil
import os
import sys

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# # Use people_list for comparison
# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()

# Use people_generator for comparison
t1 = time.process_time()
people = people_generator(1000000)
t2 = time.process_time()

print('Memory (After) : {}Mb'.format(memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))





