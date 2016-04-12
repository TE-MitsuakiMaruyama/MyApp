class MyApp:
    """
    My First Apps
    """
    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

def main():
    my_app = MyApp()
    my_app.set_name("John")
    print my_app.get_name()
    print my_app.get_name()

if __name__ == "__main__":
    main()

