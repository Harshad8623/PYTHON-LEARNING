# Link : https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"