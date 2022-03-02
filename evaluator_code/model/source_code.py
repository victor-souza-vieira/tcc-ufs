class SourceCode:
    def __init__(self, path):
        self.path = path
        self.content = []
        self.cyclomatic_complexity = []
        self.raw_metrics = []

    def print_content(self):
        print(self.content)

    def extract_content(self):
        with open(self.path, 'r') as file:
            self.content = [line for line in file]
        return self.content

    def count_code_lines(self):
        return len(self.content)
