import subprocess as sp


class RawMetrics:
    def __init__(self, path):
        self.path = path

    def calculate_raw_metrics(self):
        process_data_string = sp.getoutput('python3 -m radon raw ' + self.path + ' -j')

        return 'a'
