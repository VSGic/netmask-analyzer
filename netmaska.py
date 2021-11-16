from bin import netmask_analyzer_engine
import sys

if len(sys.argv) > 1 and len(sys.argv) < 3: 
	input_netmask = sys.argv[1]
else: 
	input_netmask = input('Input netmask for analysis:')


netmask_analyzer_engine.input_process(input_netmask)

