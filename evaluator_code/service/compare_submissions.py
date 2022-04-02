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
            # file_name = submission.extract_file_name()

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

    def compare_raw_metrics(self):
        self.base.raw_metrics_result = 'Linhas de código: {0}'.format(self.base.raw_metrics['loc'])
        for code in self.submissions:
            self.__lines_of_code_metric(code)
            self.__logical_lines_of_code_metric(code)

    def __logical_lines_of_code_metric(self, code):
        diff_lloc = code.raw_metrics['lloc'] - self.base.raw_metrics['lloc']
        alert_lloc = self.alert_config['diff_raw_metrics_lloc']
        logical_lines_of_code = code.raw_metrics['lloc']

        if 0 < diff_lloc > alert_lloc:
            # Solucao do aluno teve mais linhas de código que a do professor e ultrapassou o limite de alerta
            code.raw_metrics_result += '\n\t\t\tLinhas lógicas de código: {0}; Diferença com a submissão base: {1}; Ultrapassou o limite de alerta de {2}'.format(logical_lines_of_code, diff_lloc, alert_lloc)
            return
        if 0 < diff_lloc < alert_lloc:
            # Solucao do aluno teve mais linhas de código que a do professor, porém não ultrapassou o limite de alerta
            code.raw_metrics_result += '\n\t\t\tLinhas lógicas de código: {0}; Diferença com a submissão base: {1};'.format(logical_lines_of_code, diff_lloc)
            return
        if 0 > diff_lloc < -alert_lloc:
            # Solucao do aluno teve menos linhas de código que a do professor e ultrapassou o limite de alerta
            code.raw_metrics_result += '\n\t\t\tLinhas lógicas de código: {0}; Menos linhas que a submissão base, porém ultrapassou o limite de alerta de {1}'.format(logical_lines_of_code, alert_lloc)
            return
        if 0 > diff_lloc > -alert_lloc:
            # Solucao do aluno teve menos linhas de código que a do professor e não ultrapassou o limite de alerta
            code.raw_metrics_result += '\n\t\t\tLinhas lógicas de código: {0}; Menos linhas que a submissão base e não ultrapassou o limite de alerta'.format(logical_lines_of_code)
            return
        code.raw_metrics_result += '\n\t\t\tLinhas lógicas de código: {0}; Quantidade igual de linhas com a submissão base'.format(logical_lines_of_code)

    def __lines_of_code_metric(self, code):
        diff_loc = code.raw_metrics['loc'] - self.base.raw_metrics['loc']
        alert_loc = self.alert_config['diff_raw_metrics_loc']
        lines_of_code = code.raw_metrics['loc']

        if 0 < diff_loc > alert_loc:
            # Solucao do aluno teve mais linhas de código que a do professor e ultrapassou o limite de alerta
            code.raw_metrics_result = 'Linhas de código: {0}; Diferença com a submissão base: {1}; Ultrapassou o limite de alerta de {2}'.format(lines_of_code, diff_loc, alert_loc)
            return
        if 0 < diff_loc < alert_loc:
            # Solucao do aluno teve mais linhas de código que a do professor, porém não ultrapassou o limite de alerta
            code.raw_metrics_result = 'Linhas de código: {0}; Diferença com a submissão base: {1};'.format(lines_of_code, diff_loc)
            return
        if 0 > diff_loc < -alert_loc:
            # Solucao do aluno teve menos linhas de código que a do professor e ultrapassou o limite de alerta
            code.raw_metrics_result = 'Linhas de código: {0}; Menos linhas que a submissão base, porém ultrapassou o limite de alerta de {1}'.format(lines_of_code, alert_loc)
            return
        if 0 > diff_loc > -alert_loc:
            # Solucao do aluno teve menos linhas de código que a do professor e não ultrapassou o limite de alerta
            code.raw_metrics_result = 'Linhas de código: {0}; Menos linhas que a submissão base e não ultrapassou o limite de alerta'.format(lines_of_code)
            return
        code.raw_metrics_result = 'Linhas de código: {0}; Quantidade igual de linhas com a submissão base'.format(lines_of_code)

    def __compute_total_points_of_cyclomatic_complexity(self, complexity):
        total_points = 0
        if len(complexity) > 1:
            for function in complexity:
                total_points += function['complexity']
            return total_points

        return complexity[0]['complexity']
