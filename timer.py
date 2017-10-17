class Timer(object):
    '''
    A class that gives time difference between two time instances
    '''
    def __init__(self, name=None):
        self.name = name
        self.t_start = 0
        self.t_end = 0

    def tic(self):
        ''' timer starts '''
        self.t_start = time.time()

    def toc(self):
        ''' return timer time in seconds '''
        self.t_end = time.time()
        return self.t_end - self.t_start

    def toc_min(self):
        ''' return timer time in minutes + seconds'''
        toc_sec = toc(self)
        return np.floor(toc_sec / 60), toc_sec % 60
