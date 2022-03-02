from evaluator_code.service.cyclomatic_complexity import CyclomaticComplexity
from evaluator_code.service.raw_metrics import RawMetrics
from evaluator_code.model.source_code import SourceCode

path = '/home/victor/TCC/source-code/docs/submissions/'

sc1 = SourceCode(path + 'example.py')  # source code
sc2 = SourceCode(path + 'example2.py')  # source code

scs = [sc1, sc2]  # sources code

# -------------- CYCLOMATIC COMPLEXITY --------------
cc = CyclomaticComplexity(path, scs)
cc.calculate_complexity()

# ---------------- RAW METRICS ---------------------
rm = RawMetrics(path, scs)
rm.calculate_raw_metrics()
