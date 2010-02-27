class MediaPlayerError(Exception):
    def __init__(self):
        pass
        
class InvalidFilepathError(MediaPlayerError):
    def __init__(self):
        super(InvalidFilepathError, self).__init__()
