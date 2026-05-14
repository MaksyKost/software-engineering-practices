from abc import ABC, abstractmethod

class Platform(ABC):
    
    @abstractmethod
    
    def execute_task(self, app_name: str):
        pass

class WindowsPlatform(Platform):
    def execute_task(self, app_name: str):
        return f"Run {app_name} - Windows (.exe)"

class LinuxPlatform(Platform):
    def execute_task(self, app_name: str):
        return f"Run {app_name} - Linux (Bash)"
    
class Application(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform  

    @abstractmethod
    
    def run(self):
        pass

class LiteApp(Application):
    def run(self):
        result = self.platform.execute_task("Lite Version")
        print(f"LITE: {result} (Features are limited)")

class ProApp(Application):
    def run(self):
        result = self.platform.execute_task("Pro Version")
        print(f"PRO: {result} (Features are available)")
        
        
if __name__ == "__main__":
    windows = WindowsPlatform()
    linux = LinuxPlatform()

    app1 = LiteApp(windows)
    app2 = LiteApp(linux)
    app3 = ProApp(windows)
    app4 = ProApp(linux)

    app1.run()  
    app2.run()  
    app3.run()  
    app4.run()  