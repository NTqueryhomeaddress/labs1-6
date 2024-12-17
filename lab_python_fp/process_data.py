# process_data.py

import json
import sys
import os
import random
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

def get_json_data(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data

@print_result
def f1(data):
    job_names = list(field(data, 'job-name'))
    unique_jobs = sorted(Unique(job_names, ignore_case=True), key=lambda x: x.lower())
    return unique_jobs

@print_result
def f2(job_list):
    return list(filter(lambda x: x.lower().startswith('программист'), job_list))

@print_result
def f3(job_list):
    return list(map(lambda x: f"{x} с опытом Python", job_list))

@print_result
def f4(job_list):
    salaries = gen_random(len(job_list), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(job_list, salaries)]

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), 'data_light.json')
    
    if not os.path.exists(path):
        print(f"Файл {path} не найден.")
        sys.exit(1)
    
    data = get_json_data(path)
    
    with cm_timer_1():
        f4(f3(f2(f1(data))))
