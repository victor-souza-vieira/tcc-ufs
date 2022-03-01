from evaluator_code.model.source_code import SourceCode
from evaluator_code.service.cyclomatic_complexity import CyclomaticComplexity

# code = SourceCode('/home/victor/TCC/source-code/docs/')

cc = CyclomaticComplexity('/home/victor/TCC/source-code/docs/')
print(cc.calculate_complexity())

# code.extract_content()
# code.print_content()
# print(code.count_code_lines())
