import checksumdir

class HashGenerator():
    def __init__(self):
        pass

    def get_hash(self,path_to_dir):
        return checksumdir.dirhash(path_to_dir)