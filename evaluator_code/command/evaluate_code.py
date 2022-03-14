import json
import os

from evaluator_code.service.cyclomatic_complexity import CyclomaticComplexity
from evaluator_code.service.raw_metrics import RawMetrics
from evaluator_code.model.source_code import SourceCode

ON = "on"


def main_flow():
    configs = load_configurations()

    path = configs['root_path']

    source_codes = create_source_codes_from_path(path)

    # ------------ CYCLOMATIC COMPLEXITY -------------
    if configs['calculate_cyclomatic_complexity'] == ON:
        calculate_cyclomatic_complexity(path, source_codes)

    # ---------------- RAW METRICS ---------------------
    if configs['calculate_raw_metrics'] == ON:
        calculate_raw_metrics(path, source_codes)

    # ---------------- PRINT RESULTS -------------------
    for code in source_codes:
        code.print_attr()
        print('------------------------------------------')


def calculate_raw_metrics(path, source_codes):
    rm = RawMetrics(path, source_codes)
    rm.calculate_raw_metrics()


def calculate_cyclomatic_complexity(path, source_codes):
    cc = CyclomaticComplexity(path, source_codes)
    cc.calculate_complexity()
    calculates_the_cyclomatic_complexity_if_the_code_is_not_modularized(path, source_codes)


def calculates_the_cyclomatic_complexity_if_the_code_is_not_modularized(path, source_codes):
    for code in source_codes:
        if len(code.cyclomatic_complexity) == 0:
            file_path = code.path.replace('.py', '__CC.py')

            new_file = open(file_path, 'w')
            new_file.write('def main():\n')

            for line in code.extract_content():
                new_file.write('\t' + line)

            new_file.close()

            sc = SourceCode(file_path)
            ccc = CyclomaticComplexity(file_path, [sc])
            ccc.calculate_complexity()
            code.cyclomatic_complexity = sc.cyclomatic_complexity

            os.remove(file_path)


def create_source_codes_from_path(path):
    source_codes = []

    for directory, subdirectories, files in os.walk(path):
        for file in files:
            if ('/submissions' in directory or '/base' in directory) and ('.py' in file):
                source_code = SourceCode(os.path.join(directory, file))
                source_codes.append(source_code)

    return source_codes


def load_configurations():
    return json.load(open('../configuration/configs.json', 'r'))
