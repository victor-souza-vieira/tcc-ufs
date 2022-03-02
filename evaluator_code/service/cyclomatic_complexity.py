import subprocess as sp
import json


class CyclomaticComplexity:
    """
        Main responsibility is to calculate cyclomatic complexity using
        **radon** library.
    """

    def __init__(self, path, sources_code):
        """
        :param path: base path to files
        :param sources_code: list of SourceCode class
        """
        self.path = path
        self.sources_code = sources_code

    def calculate_complexity(self):
        """
        Calculates the cyclomatic complexity of the source codes of a given directory
        :return: List of the SourceCode class filling the cyclomatic complexity field
        """

        # Process all codes from directory and return json string with result
        process_data_string = sp.getoutput('python3 -m radon cc ' + self.path + ' -j')

        self.__extract_data(process_data_string)

        self.__clean_data()

        return self.sources_code

    def __extract_data(self, data):
        """
        :param data: string containing result process of sources code
        :return: list of SourceCode class
        """

        # convert data content to json
        data = json.loads(data[0:-4])

        # for each key in data dict
        for key in data.keys():
            # for source code in source_codes list
            for source_code in self.sources_code:
                if key == source_code.path:
                    source_code.cyclomatic_complexity = data[key]

        return self.sources_code

    def __clean_data(self):
        for source_code in self.sources_code:
            for component in source_code.cyclomatic_complexity:
                del component['endline']
                del component['lineno']
                del component['col_offset']
                del component['closures']

        return self.sources_code
