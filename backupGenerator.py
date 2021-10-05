import os
import time
from distutils.dir_util import copy_tree
from btInteractor import BTInteractor
from hashGenerator import HashGenerator


class BackupGenerator():
    _path_to_base_directory = '/Users/Surbhi.Anand/hack21'
    _path_to_original_directory = _path_to_base_directory + '/originalDirectory'
    _path_to_backup_directory = _path_to_base_directory + '/backups/backup_{}'
    _path_to_original_file = _path_to_original_directory+'/file'

    def __init__(self, freq, count):
        self._freq = freq
        self._count = count
        self._btInteractor = BTInteractor('0x282B06880c4D3AccB2E5B08DB5153C72D5cc6705', 'eb3d706e6cddae5ab379e87792579eae0c93ab288a3df7a457682eba5fd5dece')
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



