## Test environments
* local ubuntu 18.04.2, R 3.6.1
* win-builder (devel)

## R CMD check results
There were no ERRORs or WARNINGs. 

There was 1 NOTE:

* checking CRAN incoming feasibility ... NOTE
  Maintainer: ‘Austin Nar <austin.nar@gmail.com>’
  New submission

## Downstream dependencies
None (new package)

## Fixes from previous rejected submissions
* Fixed title case in DESCRIPTION file
* Added protocol 'http://' to web link in vignette tabulog.Rmd
* Added 'Value' sections to documentation
* Modified the NOT RUN sections of examples that write to disk by using tempfile()
    - These examples are now run
* Added single quotes to 'Apache' in DESCRIPTION file
