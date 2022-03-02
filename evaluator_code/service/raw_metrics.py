import json
import subprocess as sp


class RawMetrics:
    def __init__(self, path):
        self.path = path

    def calculate_raw_metrics(self):
        """
        Calculate raw metrics:
        loc = Total lines of code
        lloc = Number of logical lines of code
        sloc = Number of source lines of code
        comments = Number of python comment lines
        single_comments = Number of lines which are just comments with no code
        multi = Number of line which represent multi-line string
        blank = Number of blank lines or whitespace only

        equation: loc = sloc + blanks + multi + single_comments
        :return:
        """
        process_data_string = sp.getoutput('python3 -m radon raw ' + self.path + ' -j')

        process_data_json = json.loads(process_data_string[0:-4])
        return 'a'
