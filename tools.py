from datetime import datetime


def timed_step(label, func, *args, print_results: bool = True, **kwargs):
    start = datetime.now()
    print(f"{label}: ", end='', flush=True)
    result = func(*args, **kwargs)
    end = datetime.now()
    step_time = end - start
    result_str = f"{result}. " if print_results else ""
    print(f"{result_str}Done in {step_time.total_seconds() * 1000:.6f} milliseconds")
    return result


def timed_step_check(label, func, expected, *args, **kwargs):
    start = datetime.now()
    print(f"{label}: ", end='', flush=True)
    result = func(*args, **kwargs)
    end = datetime.now()
    step_time = end - start
    if result == expected:
        print("✅ Test passed!", end=' ')
    else:
        print(f"❌ Test failed! Expected {expected}, but got {result}", end=' ')
    print(f"Done in {step_time.total_seconds() * 1000:.6f} milliseconds")
