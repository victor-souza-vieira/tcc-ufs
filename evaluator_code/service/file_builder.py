new_line = '\n'
tab = '\t'
two_tabs = '\t\t'
three_tabs = '\t\t\t'
four_tabs = '\t\t\t\t'


class FileBuilder:
    def __init__(self, problems, source_codes, output='/home/victor/TCC/source-code/docs/result.txt'):
        self.problems = problems
        self.source_codes = source_codes
        self.output = output

    def build(self):
        with open(self.output, 'w', encoding='UTF-8') as output:
            for problem in self.problems:
                header_problem = '--------------- Resultados para o problema: `{0}`. --------------- {1}{2}'.format(problem, new_line, tab)
                body_problem = ''
                for code in self.source_codes:
                    if code.extract_problem_name() == problem:
                        if code.is_base_source_code():
                            header_problem += 'Resultado para a solução base:' + new_line + two_tabs
                            header_problem += code.cyclomatic_complexity_result + new_line + two_tabs
                            header_problem += code.raw_metrics_result + new_line + tab
                            header_problem += 'Resultado para as submissões dos alunos:' + new_line + two_tabs
                            continue
                        body_problem += 'Submissão: ' + code.extract_file_name() + new_line + three_tabs
                        body_problem += 'Complexidade ciclomática: ' + code.cyclomatic_complexity_result + new_line + three_tabs
                        body_problem += code.raw_metrics_result + new_line + two_tabs
                output.write(header_problem)
                output.write(body_problem)
                output.write(new_line)
