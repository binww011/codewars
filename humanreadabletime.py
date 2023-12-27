from math import *

def make_readable(seconds):
    hours = floor(seconds/3600)
    seconds -= hours*3600
    minutes = floor(seconds/60)
    seconds -= minutes*60
    
    return f"{f'0{hours}' if hours < 10 else hours}:{f'0{minutes}' if minutes < 10 else minutes}:{f'0{seconds}' if seconds < 10 else seconds}"
