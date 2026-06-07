from kernel import Kernel

class Shell:
    def __init__(self, kernel):
        self.kernel = kernel
        self.version = "0.0.1"

    def run(self):
        print("Kernel loadded successfully")
        while self.kernel.running:
            cmd = input(">>> ").strip()
            self.execute(cmd)    

    def execute(self, cmd):
        if cmd in ("Help", "help", "h"):
            self.kernel.write(1, "Available: help, about, version, poweroff")
        elif cmd in ("Version", "version", "ver", "v"):
            self.kernel.write(1, f"Kernel: {self.kernel.version}, Shell: {self.version}")               
        elif cmd in ("About", "about"):
            self.kernel.write(1, "About text")
        elif cmd in ("Poweroff", "poweroff", "Off", "off"):
            self.kernel.running = False
        else:
            self.kernel.write(1, f"Unknown command: {cmd},try help")