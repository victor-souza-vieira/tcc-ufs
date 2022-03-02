from evaluator_code.service.cyclomatic_complexity import CyclomaticComplexity
from evaluator_code.service.raw_metrics import RawMetrics


path = '/home/victor/TCC/source-code/docs/'
cc = CyclomaticComplexity(path)
print(cc.calculate_complexity())

rm = RawMetrics(path)
rm.calculate_raw_metrics()
