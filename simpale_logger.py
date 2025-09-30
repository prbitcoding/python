class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'a')    
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileLogger('log.txt') as log:
    log.write('Logging a message\n')

print("Log written to 'log.txt'")
