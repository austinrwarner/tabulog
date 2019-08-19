---
title: 'tabulog: A Language-Agnostic Template System or Parsing Log Files'
tags:
  - Python
  - R
  - text processing
authors:
  - name: Austin Nar
    orcid: 0000-0002-5319-9805
date: 18 August 2019
bibliography: paper.bib
---

# Summary

Log files (such as Apache's ``access.log`` files) often have a very regular 
structure with the same fields in each log entry. The format of these log
files is usually optimized for human-readability as opposed to machine-readability.
For data scientists and others who wish to perform analytics on thses log files,
the ability to easily convert files into a tabular format is necessary to gain any 
meaningful insight regarding the contents of individual fields of the log file.

While for a single log format most data scientists and endgineers should be able
to extract individual data elements from such files, solutions are often a messy
patchwork of regex extracts that have poor-to-mediocre code readability. Also, for
those who wish to analyze the log files of various formats from different
sources, the need to reinvent the wheel for each new format is an unnecessary
bottleneck that gets in the way of working on the actual analysis.

``tabulog`` is a language-agnostic template syntax for parsing log files, with
libraries today for ``Python`` and ``R``. The ``tabulog`` syntax is influnced by 
the Jinja2 template library in Python. Parsing a log file is as simple as 
writing a template, which defines the structure of a line in a log file, and 
defining the regex patterns that a field in the log record should match. In order 
to be portable and self-contained, the entire definition of this operation can
be stored in a human-readable ``YAML`` file, which makes it easy to port the parsing
logic between ``Python`` and ``R``. 

``tabulog`` as a syntax is designed to be language agnostic, but is heavily 
influenced by ``Jinja2`` [@jinja2]. The ``R`` [@R] package is dependent on the
package ``yaml`` [@yaml], and the ``Python`` [@python] package is dependent on
the package ``PyYAML`` [@pyyaml]. In both cases ``YAML`` is used for reading 
``tabulog`` templates which are stored in ``YAML`` files for use with either
``R`` or ``Python``. The ``Python`` package is also dependent on Pandas [@pandas],
whose ``DataFrame`` class is 'tabular format' that is used for the final output
in ``Python``. The project is designed for data scientists who want
a quick, clean, reproducible way of converting semi-structured log files into
a tabular format that is easy to use for analysis.


# References