class SourceCode:
    def __init__(self, path, cyclomatic_complexity):
        self.path = path
        self.content = []
        self.cyclomatic_complexity = cyclomatic_complexity

    def print_content(self):
        print(self.content)

    def extract_content(self):
        with open(self.path, 'r') as file:
            self.content = [line for line in file]
        return self.content

    def count_code_lines(self):
        return len(self.content)
