class Savetofile:
    @staticmethod
    def write(filename: str, data: str):
        with open(filename, mode='wb') as file:
            file.write(data)
