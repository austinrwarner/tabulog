_identity = lambda x: x

class Parser:
  """This is a helper class that represents a given field in the tabulog template. 
  
  Parser objects have a regex string (pattern) to match for in the record, a formatter
  function which takes the extracted text for the field and modifies it in some way 
  (ex. cast to integer, make lowercase, etc.), and an optional name.
  
  Attributes:
    - pattern (str): regex string to match on in the template
    - formatter (callable): Callable (usually a function or lambda expression) to
      modify the field after extraction
    - name (str): optional name for identification
  """
  def __init__(self, pattern, formatter = _identity, name = None):
    """Parser constructor
    
    Args:
      - pattern (str): regex string to match on in the template
      - formatter (callable): Callable (usually a function or lambda expression) to
        modify the field after extraction
      - name (str): optional name for identification
        
    """
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
