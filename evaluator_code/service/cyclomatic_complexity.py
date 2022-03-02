import subprocess as sp
import json
from evaluator_code.model.source_code import SourceCode


class CyclomaticComplexity:
    """
        Main responsibility is to calculate cyclomatic complexity using
        **radon** library.
    """
    def __init__(self, path):
        self.path = path

    def calculate_complexity(self):
        """
        Calculates the cyclomatic complexity of the source codes of a given directory
        :return: List of the SourceCode class filling the cyclomatic complexity field
        """

        # Process all codes from directory and return json string with result
        process_data_string = sp.getoutput('python3 -m radon cc ' + self.path + ' -j')

        sources_code = self.__extract_data(process_data_string)

        sources_code = self.__clean_data(sources_code)

        return sources_code

    @staticmethod
    def __extract_data(data):
        """
        :param data: string containing result process of sources code
        :return: list of SourceCode class
        """

        # convert data content to json
        data = json.loads(data[0:-4])

        # list of source code
        sources_code = []

        # for each key in data dict
        for key in data.keys():
            # filling SourceCode object
            source_code = SourceCode(key, data[key])

            # add SourceCode object into sources_code list
            sources_code.append(source_code)

        return sources_code

    @staticmethod
    def __clean_data(sources_code):
        for source_code in sources_code:
            for component in source_code.cyclomatic_complexity:
                del component['endline']
                del component['lineno']
                del component['col_offset']
                del component['closures']

        return sources_code
