import os
import time
from distutils.dir_util import copy_tree
from btInteractor import BTInteractor
from hashGenerator import HashGenerator


class BackupGenerator():
    _path_to_base_directory = '/Users/animesh.kumar/hackathon'
    _path_to_original_directory = _path_to_base_directory + '/originalDirectory'
    _path_to_backup_directory = _path_to_base_directory + '/backups/backup_{}'
    _path_to_original_file = _path_to_original_directory+'/file'

    def __init__(self, freq, count):
        self._freq = freq
        self._count = count
        self._btInteractor = BTInteractor('0x34E7e0A4d8dED9448e04Ee0f1819595CD9De46f4', 'd94b93442e0b2ef1a71b84e633637f923357dc9966065abc8ea5a67027850aad')
        self.hashGenerator = HashGenerator()

    def delta_change(self, counter):
        file_object = open(self._path_to_original_file,'a')
        file_object.write(f'Change for counter {counter} \n')
        file_object.close()

    def take_backup(self, counter):
        backup_path = self._path_to_backup_directory.format(counter)
        copy_tree(self._path_to_original_directory, backup_path)
        print(f'done backup for counter {counter}')
        self.insert_hash_to_blockchain(backup_path)

    def insert_hash_to_blockchain(self, path):
        hash_val = self.hashGenerator.get_hash(path)
        self._btInteractor.addHashToBlockchain(hash_val,path)

    def start(self):
        for counter in range(self._count):
            time.sleep(self._freq)
            self.delta_change(counter)
            self.take_backup(counter)


if __name__ == '__main__':
    bg = BackupGenerator(5,5)
    bg.start()



