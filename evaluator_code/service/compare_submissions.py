class CompareSubmissions:
    def __init__(self, base, submissions, alert_config):
        self.base = base
        self.submissions = submissions
        self.alert_config = alert_config

    def compare_cyclomatic_complexity(self):
        base_complexity = self.__compute_total_points_of_cyclomatic_complexity(self.base.cyclomatic_complexity)
        self.base.cyclomatic_complexity_result = 'Complexidade ciclomática: {0} pontos.'.format(base_complexity)

        for submission in self.submissions:
            submission_total_complexity = self.__compute_total_points_of_cyclomatic_complexity(submission.cyclomatic_complexity)

            diff = submission_total_complexity - base_complexity
            alert = self.alert_config['diff_cyclomatic_complexity']
            file_name = submission.extract_file_name()

            if 0 < diff > alert:
                # Aqui a submissao do aluno teve complexidade maior que a do professor baseado na configuração de alerta
                submission.cyclomatic_complexity_result = '{0} pontos com diferença de {1} pontos com a solução base ultrapassando o limite de alerta de {2} pontos'.format(submission_total_complexity, diff, alert)
                continue
            if 0 > diff > -alert:
                # Aqui a submissao do professor teve uma complexidade ciclomatica geral maior do que a do aluno passando do nivel de alerta
                submission.cyclomatic_complexity_result = '{0} pontos com diferença de {1} pontos com a solução base ultrapassando o limite de alerta de  -{2} pontos.'.format(submission_total_complexity, diff, alert)
                continue
            if 0 < diff < alert:
                # Aqui a submissao do aluno teve maior complexidade que a do professor, porém não passou do nivel de alerta
                submission.cyclomatic_complexity_result = '{0} pontos contra {1} da solução base.'.format(submission_total_complexity, base_complexity)
                continue
            if 0 > diff > -alert:
                # Aqui a submissao do aluno teve menor complexidade que a do professor, porém não passou do nivel de alerta
                submission.cyclomatic_complexity_result = '{0} pontos contra {1} da solução base'.format(submission_total_complexity, base_complexity)
                continue

            submission.cyclomatic_complexity_result = '{0} pontos, igual a solução base'.format(submission_total_complexity)

    def __compute_total_points_of_cyclomatic_complexity(self, complexity):
        total_points = 0
        if len(complexity) > 1:
            for function in complexity:
                total_points += function['complexity']
            return total_points

        return complexity[0]['complexity']
