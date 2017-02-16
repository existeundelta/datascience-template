import os
import sys

cwd = os.path.dirname(os.path.realpath(__file__))
src = os.path.join(cwd, '..', 'src')
models = os.path.join(cwd, '..', 'models')

if src not in sys.path:
    sys.path.insert(1, src)
