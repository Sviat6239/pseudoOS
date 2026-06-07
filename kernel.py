class Kernel:
    def __init__(self):
        self.running = True
        self.stdout = 1
        self.version = "0.0.2"

    def write(self, fd, message):
        if fd == 1:
            print(message)


if __name__ == "__main__":
    from shell import Shell

    kernel = Kernel()
    shell = Shell(kernel)
    shell.run()