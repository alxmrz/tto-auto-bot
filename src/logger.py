class Logger:
    def __init__(self, enable: bool):
        self.need_log = enable

    def info(self, *args: object) -> None:
        if self.need_log:
            print(*args)
