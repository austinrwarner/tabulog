import os
import yaml
from .parser import Parser, _identity as identity
from collections import defaultdict

def _default_formatters():
  """List of formatters provided 'out-of-the-box' for use with default classes"""
  d = defaultdict(lambda: identity)
  defaults = [
    ('int',    int  ),
    ('double', float)
  ]
  for k,v in defaults:
    d[k] = v
    
  return(d)

def default_classes():
  """A dictionary of default Parser classes provided 'out-of-the-box'.
  
  By 'classes' here we mean Parser objects that come predefined with a defining regex string,
  and possibly a meaningful formatter function.

  Returns:
    A dictionary of Parser objects

  >>> default_classes()
  {'ip': Parser('[0-9]{1,3}(\.[0-9]{1,3}){3}', <function <lambda> at 0x7f492c4426a8>, 'ip')...
  

  """
  (path, file) = os.path.split(__file__)
  conf_file = os.path.join(path, 'config', 'parser_classes.yml')
  with open(conf_file, 'r') as f:
    conf = yaml.safe_load(f)
  formatters = _default_formatters()
  
  parsers = { key:Parser(conf[key], formatters[key], key) for key in conf }
  return(parsers)
  
