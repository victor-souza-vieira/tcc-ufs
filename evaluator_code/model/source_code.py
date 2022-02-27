class SourceCode:
    def __init__(self, path):
        self.path = path
        self.content = []

    def print_content(self):
        print(self.content)

    def extract_content(self):
        with open(self.path, 'r') as file:
            for line in file:
                self.content.append(line)
        return self.content

    def count_code_lines(self):
        return len(self.content)
