from time import time

LOGGER_INIT_TIME = time()


def get_time():
    return round(time() - LOGGER_INIT_TIME, 3)


def log_str(info: str, start: str = ">>> ", end: str = "\n"):
    return f"{get_time():.3f} {start}{info}{end}"


if __name__ == "__main__":
    print(log_str("hello"))
