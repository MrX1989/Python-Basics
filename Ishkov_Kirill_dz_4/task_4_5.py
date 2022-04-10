import sys
from task_4_4_prog import currency_rates

parametr = sys.argv
result = parametr.pop(1)
currency_rates(result.upper())
