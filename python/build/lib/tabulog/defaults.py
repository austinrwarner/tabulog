import os
import yaml
from .parser import Parser, _identity as identity
from collections import defaultdict

# List of formatters provided "out-of-the-box" for use with default classes
def _default_formatters():
  d = defaultdict(lambda: identity)
  defaults = [
    ('int',    int  ),
    ('double', float)
  ]
  for k,v in defaults:
    d[k] = v
    
  return(d)

def default_classes():
  (path, file) = os.path.split(__file__)
  conf_file = os.path.join(path, 'config', 'parser_classes.yml')
  with open(conf_file, 'r') as f:
    conf = yaml.safe_load(f)
  formatters = _default_formatters()
  
  parsers = { key:Parser(conf[key], formatters[key], key) for key in conf }
  return(parsers)
  
