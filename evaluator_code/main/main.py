from evaluator_code.service.cyclomatic_complexity import CyclomaticComplexity

cc = CyclomaticComplexity('/home/victor/TCC/source-code/docs/')
print(cc.calculate_complexity())
