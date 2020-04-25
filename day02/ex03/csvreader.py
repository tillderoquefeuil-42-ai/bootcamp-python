import os.path


class CsvReader():
    def __init__(self, filename='', sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.delimiter = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

        self.__header = None
        self.__data = []

        self.file = None

    def __enter__(self):
        if not os.path.exists(self.filename):
            return None

        self.file = open(self.filename)
        if not self.read():
            return None
        return self
    
    def __exit__(self, type, value, traceback):
        if self.file:
            self.file.close

    def read(self):
        lines = self.file.readlines()

        count = 0
        size = 0
        skip_bottom = len(lines) - self.skip_bottom

        for line in lines:
            l = list(line.strip().split(self.delimiter))
            l = list(map(lambda x: x.strip(), l))

            if count == 0:
                self.__header = l
                size = len(l)
            elif size != len(l):
                return None

            if self.header == True and count == 0:
                self.__data.append(l)
            elif self.header == False and count == 0:
                pass
            elif self.skip_top <= count and count < skip_bottom:
                self.__data.append(l)
            count += 1
        return True

    def getdata(self):
        return self.__data

    def getheader(self):
        return self.__header



# with CsvReader('good.csv') as file:
#     if file == None:
#         print("File is corrupted")
#     else:
#         header = file.getheader()
#         data = file.getdata()
#         print(header)
#         print(data)

# with CsvReader('bad.csv') as file:
#     if file == None:
#         print("File is corrupted")
#     else:
#         header = file.getheader()
#         data = file.getdata()
#         print(header)
#         print(data)