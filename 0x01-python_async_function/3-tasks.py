#!/usr/bin/env python3
""" This module contains the function task_wait_random"""


from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Arg: max_delay - max time the wait random will delay
    return: task - an async task"""
    task: Task = create_task(wait_random(max_delay))
    return task
