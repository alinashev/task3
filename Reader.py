import json

class Reader:
    def __int__(self, path):
        self.path = path

    def openJSONFile(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            text = json.load(f)
        return text