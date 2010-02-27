import os

class File(object):
    def __init__(self, path):
        if os.path.isfile(path):
            self._path = path
        else:
            raise InvalidFilePathError
            
    def get_path(self):
        return self._path
        
class MediaFile(File):
    def __init__(self, path):
        super(MediaFile, self).__init__(path)
