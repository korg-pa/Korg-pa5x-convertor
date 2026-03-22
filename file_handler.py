import os
import json

class FileHandler:
    def __init__(self, directory):
        self.directory = directory

    def find_files(self, extension):
        return [f for f in os.listdir(self.directory) if f.endswith(extension)]

    def read_file(self, filename):
        path = os.path.join(self.directory, filename)
        with open(path, 'r') as file:
            return file.read()

    def create_json_config(self, filename, data):
        path = os.path.join(self.directory, filename)
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)