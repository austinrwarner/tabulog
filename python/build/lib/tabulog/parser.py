_identity = lambda x: x

class Parser:
  def __init__(self, pattern, formatter = _identity, name = None):
    if type(pattern) is Parser:
      formatter = pattern.formatter
      name      = pattern.name
      pattern   = pattern.pattern
    
    self.pattern   = pattern
    self.formatter = formatter
    self.name      = name
  
  def __repr__(self):
    if self.name:
      r = "Parser('{}', {}, '{}')".format(self.pattern, self.formatter, self.name)
    else:
      r = "Parser('{}', {})".format(self.pattern, self.formatter)
    return(r)
