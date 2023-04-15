import importlib
import sys
import os
import vera

# Change the working directory to the directory of the script
module_source_folder = os.path.dirname(sys.argv[0])
os.chdir(module_source_folder)

# Load the source file
vera.loadTokens(open(sys.argv[1]).read(), sys.argv[2])
vera.setSourceFileNames([sys.argv[2]])

# Load the modules
modules = open('modules.conf').readlines()

# Run the modules
for module in modules:
    if module[-1] == '\n':
        module = module[:-1]
    try:
        importlib.import_module(module)
    except:
        pass

# Print the reports
vera.logReports()
