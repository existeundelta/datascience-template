import glob, os
from wrapper import *
import importlib
import sys

try:
    import cpickle as pickle
except:
    import pickle

from sklearn.externals import joblib
import jsonpickle


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def load_custom_models():
    cwd = os.path.dirname(os.path.abspath(__file__))
    lookup = os.path.join(cwd, "*.py")

    for filepath in glob.glob(lookup):
        with open(filepath, 'rb') as fp:
            basename = os.path.basename(filepath)
            basename = os.path.splitext(basename)[0]

            if basename != "__init__" and basename != "wrapper":
                yield basename

def get_models(ext, loader):
    cwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cwd, '..', '..', 'models')
    lookup = os.path.join(path, "*." + ext)

    for filepath in glob.glob(lookup):
        with open(filepath, 'rb') as fp:
            basename = os.path.basename(filepath)
            basename = os.path.splitext(basename)[0]

            yield basename, loader.load(fp)


## INJECT LOCAL WRAPPERS
for module in load_custom_models():
    globals()[module] = __import__("models." + module, locals=None, globals=None, fromlist=[None])
    # TODO: This hotfix might just be removed, must be tested
    for name in dir(globals()[module]):
        attr = getattr(globals()[module], name)
        setattr(sys.modules["__main__"], name, attr)


# Load modules
pkl_models = dict(get_models("pkl", pickle))
jlb_models = dict(get_models("jlb", joblib))
json_models = dict(get_models("json", jsonpickle))
models = merge_two_dicts(merge_two_dicts(pkl_models, jlb_models), json_models)

