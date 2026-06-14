class Logger:
    def __init__(self, enable: bool):
        self.need_log = enable

    def info(self, *args):
        if self.need_log:
            print(*args)
