class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class FileSystemSimulator:
    def __init__(self, capacity):
        self.capacity = capacity
        self.free_space = capacity
        self.files = []

    def add_file(self, file):
        if file.size > self.free_space:
            print("Not enough free space to add the file")
            return
        self.files.append(file)
        self.free_space -= file.size

    def remove_file(self):
        if not self.files:
            print("No files to remove")
            return
        file = self.files.pop(0)
        self.free_space += file.size

    def print_files(self):
        if not self.files:
            print("No files in the file system")
        else:
            print("Files in the file system:")
            for file in self.files:
                print(file.name, file.size)

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the file system: "))
    file_system = FileSystemSimulator(capacity)

    while True:
        print("\nFile System Simulator Menu:")
        print("1. Add a file")
        print("2. Remove a file")
        print("3. Display files")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter the name of the file: ")
            size = int(input("Enter the size of the file: "))
            new_file = File(name, size)
            file_system.add_file(new_file)
        elif choice == '2':
            file_system.remove_file()
        elif choice == '3':
            file_system.print_files()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
