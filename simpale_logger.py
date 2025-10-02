class FileLogger:
    def __init__(self, file1):
        self.file1 = file1

    def __enter__(self):
        self.file = open(self.file1, 'a')    
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileLogger('log.txt') as log:
    log.write('Logging a message\n')

print("Log written to 'log.txt'")
