class CompareSubmissions:
    def __init__(self, base, submissions, alert_config):
        self.base = base
        self.submissions = submissions
        self.alert_config = {'diff_cyclomatic_complexity': 5}

    def compare_cyclomatic_complexity(self):
        base_complexity = self.__compute_total_points_of_cyclomatic_complexity(self.base.cyclomatic_complexity)

        for submission in self.submissions:
            submission_total_complexity = self.__compute_total_points_of_cyclomatic_complexity(submission.cyclomatic_complexity)

            if 0 < (submission_total_complexity - base_complexity) > self.alert_config['diff_cyclomatic_complexity']:
                # TODO aqui a submissao do aluno teve complexidade maior que a do professor baseado na configuração de alerta
                print(1)
                continue
            if 0 > (submission_total_complexity - base_complexity) > -self.alert_config['diff_cyclomatic_complexity']:
                # TODO aqui a submissao do professor teve uma complexidade ciclomatica geral maior do que a do aluno passando do nivel de alerta
                print(2)
                continue
            if 0 < (submission_total_complexity - base_complexity) < self.alert_config['diff_cyclomatic_complexity']:
                # TODO aqui a submissao do aluno teve maior complexidade que a do professor, porém não passou do nivel de alerta
                print(3)
                continue
            if 0 > (submission_total_complexity - base_complexity) > -self.alert_config['diff_cyclomatic_complexity']:
                # TODO aqui a submissao do aluno teve menor complexidade que a do professor, porém não passou do nivel de alerta
                print(4)
                continue
            print(5)  # TODO tiveram a mesma pontuação

    def __compute_total_points_of_cyclomatic_complexity(self, complexity):
        total_points = 0
        if len(complexity) > 1:
            for function in complexity:
                total_points += function['complexity']
            return total_points

        return complexity[0]['complexity']
