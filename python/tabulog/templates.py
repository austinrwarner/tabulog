import yaml, re, os
from pandas import DataFrame as DF

from .defaults import default_classes
from .parser import Parser, _identity as identity



class Template:
  
  def __init__(self, template_string=None, file=None, classes=[]):
    
    self.classes = default_classes()
    
    if template_string:
      if type(template_string) != str:
        raise TypeError("'template_string' must be type 'str'")
        
      self.template = template_string
      self.custom_classes = classes
      for c in classes:
        if type(c) != Parser:
          raise TypeError("'classes' must be a list of 'Parser' objects.")
        self.classes[c.name] = c
        
    elif file:
      if not os.path.exists(file):
        raise OSError("File '{}' not found".format(file))
      
      with open(file, 'r') as f:
        conf = yaml.safe_load(f)
        
      try:
        classes = conf['classes']
      except KeyError:
        pass
        
      classes = [Parser(pattern, name=name) for (name, pattern) in classes.items()]
      
      self.template = conf['template']
      self.__init__(conf['template'], classes = classes)
        
    else:
      raise ValueError("Either 'template_string' or 'file' must be not None")
    
  
  def __repr__(self):
    return('Template("{}", classes = ...)'.format(self.template.replace('"', r'\"')))
  
    
  def tabulate(self, text):
    
    def extract(text, parser):
      if type(text) != str:
        raise TypeError("'text' must be of type 'str'")
      if type(parser) != Parser:
        raise TypeError("'parser' must be a 'Parser' object")
      
      (begin,end) = re.search(parser.pattern, text).span()
      return((parser.formatter(text[begin:end]), text[end:]))
    
    template = self.template.replace('\{', '&#123;').replace('\}', '&#125;')
    template = re.split('\\{(?=\\{)|(?<=\\})\\}', template)
    
    fields = []
    for field in template:
      if re.match('^\{.*\}$', field):
        (field_class, field_name) = re.split('\s+', re.sub('^\\{\\s*|\\s*\\}$', '', field))
        p = self.classes[field_class]
      else:
        field = re.escape(field)
        field_name = None
        p = Parser(field)
      
      if len(p.pattern) > 0: 
        fields.append((field_name, p))
    
    table = {}
    while len([name for (name, parser) in fields if name]) > 0:
      lookbehind = '^'
      lookahead  = ''
      
      next_field = [i for i in range(len(fields)) if fields[i][0]][0]
      
      (name,parser) = fields[next_field]
      
      if next_field > 0:
        lookbehind = "(?<=^{})".format(
          ''.join([ parser.pattern for (name, parser) in fields[:next_field]])
        )
      if next_field < len(fields) - 1:
        if not fields[next_field+1][0]:
          lookahead = "(?={})".format(fields[next_field+1][1].pattern)
      
      pattern = "{}{}{}".format(lookbehind, parser.pattern, lookahead)
      parser = Parser(pattern, parser.formatter)
      
      extracted = [ extract(t, parser) for t in text ]
      
      parsed = [ parsed for (parsed, text) in extracted ]
      text = [ text for (parsed, text) in extracted ]
      
      if(next_field == len(fields)):
        break
      else:
        fields = fields[next_field+1:]
      table[name] = parsed
    
    return(DF(table))
      
        
