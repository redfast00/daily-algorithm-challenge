import hashlib
import os

# Challenge: sync files in a low-bandwidth environment, if most of the files are already synced
# This code just captures the idea of what I would implement


class Syncer():
    def __init__(self, directory):
        self.directory = directory

    def request(self, path):
        with open(path, 'rb') as infile:
            return infile.read()

    def write(self, path, data):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as outfile:
            outfile.write(data)

    def list(self):
        for root, dirs, files in os.walk(self.directory):
            for name in files:
                path = os.path.join(root, name)
                hasher = hashlib.sha1()
                hasher.update(self.request(path))
                digest = hasher.hexdigest()
                yield path, digest

    def sync_from(self, other):
        own_files = set(self.list())
        for path, digest in other.list():
            if (path, digest) not in own_files:
                self.write(path, other.request(path))
