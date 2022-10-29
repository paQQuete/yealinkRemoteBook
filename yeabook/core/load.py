import os

class Savetofile:
    @staticmethod
    def write(filename: str, data: bytes, dirname: str = 'files'):
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        os.chdir(dirname)
        with open(filename, mode='wb') as file:
            file.write(data)
