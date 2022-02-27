from evaluator_code.model.source_code import SourceCode

code = SourceCode('/home/victor/TCC/source-code/docs/example.py')

code.extract_content()
code.print_content()
print(code.count_code_lines())
