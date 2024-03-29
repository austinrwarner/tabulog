
An Example in Python
--------------------

Let's again say you have the example logs in the file `accesslog.txt`.

    10.0.0.8 - - [2019-01-01:10:58:12 -0500] "https://mysite.com/index.html"
    173.28.102.33 - - [2019-01-01:10:58:25 -0500] "https://mysite.com/login"

We first define the template.

``` python
template = '{{ ip ip_address }} - - [{{ date date_time }}] "{{ url URL }}"'
```

We then need to define our classes. `ip` and `url` are builtins with the package, but dates come in a variety of formats so we must explicitly define ours here. Note you can see all builtins using `default_classes()`

``` python
import tabulog, datetime 

date_parser = tabulog.Parser(
  '[0-9]{4}\\-[0-9]{2}\\-[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{2}[ ][\\-\\+][0-9]{4}',
  lambda x:datetime.datetime.strptime(x, '%Y-%m-%d:%H:%M:%S %z'),
  name = 'date'
)
date_parser
```

    Parser('[0-9]{4}\-[0-9]{2}\-[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{2}[ ][\-\+][0-9]{4}', <function <lambda> at 0x7f7a07574e18>, 'date')

``` python
for key in ['ip', 'url']:
  print(tabulog.default_classes()[key])
```

    Parser('[0-9]{1,3}(\.[0-9]{1,3}){3}', <function <lambda> at 0x7f7a06c896a8>, 'ip')
    Parser('(-|(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+)', <function <lambda> at 0x7f7a06c896a8>, 'url')

Both `ip` and `url` require no formatting, so they have the identity function, (`lambda x:x` in python), as their formatter.

To get our final output in tabular format, we first combine everything into a `Template` object.

``` python
# We only need to pass our custom date parser class, the defaults will be included.
T = tabulog.Template(
  template_string = template,
  classes = [date_parser]
)
T
```

    Template("{{ ip ip_address }} - - [{{ date date_time }}] \"{{ url URL }}\"", classes = ...)

Note that we only had to pass our custom class `date`. The builtin classes `ip` and `url` were included by default.

Finally, we can read in our log file, and call the `tabulate` function in our `Template` object. The 
final output is a Pandas DataFrame.

``` python
with open('accesslog.txt', 'r') as f:
  logs = f.read().split('\n')[:-1]

T.tabulate(logs)
```

          ip_address                 date_time                            URL
    0       10.0.0.8 2019-01-01 10:58:12-05:00  https://mysite.com/index.html
    1  173.28.102.33 2019-01-01 10:58:25-05:00       https://mysite.com/login


A more elegant and portable way of completing this task would be to define the template and the custom class in the same file, which can be ported to other Tabulog libraries in other languages, leaving only the formatters to be defined in the R script.

First, we define the `template` and the `classes` in a yaml file

```
~$ cat accesslog_template.yml
```

    template: '{{ ip ip_address }} - - [{{ date date_time }}] "{{ url URL }}"'
    classes:
      date: '[0-9]{4}\-[0-9]{2}\-[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{2}[ ][\-\+][0-9]{4}'

Next, we define the formatters for each of our classes. Here we only have one, but we still put it in a named list, with the name matching the name of the class in the template file.

``` python
formatters = {
  'date': lambda x:datetime.datetime.strptime(x, '%Y-%m-%d:%H:%M:%S %z')
}
```

Next, we make create our template again, this time using the `file` argument.

``` r
T = tabulog.Template(
  file = 'accesslog_template.yml',
  formatters = formatters
)
T
```

    Template("{{ ip ip_address }} - - [{{ date date_time }}] \"{{ url URL }}\"", classes = ...)

Again, we get our final output with the same call to `tabulate`.

``` python
T.tabulate(logs)
```

          ip_address                 date_time                            URL
    0       10.0.0.8 2019-01-01 10:58:12-05:00  https://mysite.com/index.html
    1  173.28.102.33 2019-01-01 10:58:25-05:00       https://mysite.com/login
