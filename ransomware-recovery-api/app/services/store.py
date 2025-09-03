class InMemoryStore:
    def __init__(self):
        self.files = {}

    def add_file(self, filename, status="clean", notes=None):
        self.files[filename] = {"filename": filename, "status": status, "notes": notes}
        return self.files[filename]

    def get_file(self, filename):
        return self.files.get(filename)

    def list_files(self):
        return list(self.files.values())

    def delete_file(self, filename):
        return self.files.pop(filename, None) is not None

store = InMemoryStore()
