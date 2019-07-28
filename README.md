# tabulog
Parsing Semi-Structured Log Files into Tabular Format

## Introduction to Tabulog

Tabulog is a flexible, powerful framework for parsing log files, specifically
designed for web logs (such as the access.log files created by Apache), with the
final output being in a tabular format.

Parsing logs with Tabulog requires two things: a template, and a list of
"parser classes."

### Tabulog Templates

Inspired by Python's [Jinja2 templates](jinja.pocoo.org/), Tabulog templates
use a human-readable format mixing literal text with code. Code is being used
extremely loosely here, as you will see that the 'code' in our templates
is not actually R code. 

The easiest place to start is with an example. Let's say you have a simple log 
file that looks like this:

```
10.0.0.8 - - [2019-01-01:10:58:12 -500] "https://mysite.com/index.html"
173.28.102.33 - - [2019-01-01:10:58:25 -500] "https://mysite.com/login"
...
```

We can see the log file here holds a certain format, specifically:

```
<ip address> - - [<datetime>] "<url>"
```

The Tabulog template to parse such a file looks like this

```
{{ ip ip_address }} - - [{{ Date date_time }}] "{{ url URL }}"
```

Each set of curly brackets represents an instance of a *class*, and is declared 
in the C style of `class var_name`. So in the template above, `{{ ip ip_address }}`
is really saying "In this spot, look for an ip, and call it `ip_address`."

You may ask, how does the Tabulog know what an ip address *is*? Which is where
we are introduced to *parser classes*.

### Parser Classes
In order to know what to look for in each field of our template, Tabulog must 
know what a given class should look like. For this we give it a *parser class*,
which is really just a wrapper object for a regular expression.

In the current example with the ip address, we would tell Tabulog that the
ip class is represented by the Perl regular expression: `[0-9]{1,3}(\.[0-9]{1,3}){3}`.
When Tabulog parsed the log file, it would look for a match on that expression
in that spot, and raise a warning if it didn't find one.

#### Parser Formatters
Once a field is parsed , you may want to further transform or 
*format* the text. For example, you may want to cast an integer. This is 
achieved using formatters.

When a parser object is created, an optional formatter can be passed. This is
simply a function that taking the extracted field of text and returining
the transformed field.

Tabulog as a framework is designed to be language-agnostic, so the ideas of
templates and parser classes here will be portable between languages. Formatters, 
however, are languagespecific and must be implemented in the language being used. 


## Notes

### Escape characters
The only characters that need to be escaped in templates are curly braces 
(even single ones). Usually a backslash should be sufficient `'\{'`, but the 
html-style escapes `'&#123;'` and `'&#125;'` are also included as valid syntax
for any edge cases that may arise.