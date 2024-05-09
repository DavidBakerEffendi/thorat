# Benchmark for Taint Analysis Tools for Python

A benchmark to study the available taint-analysis tools for Python. This repository originally came from 
[benchmark-for-taint-analysis-tools-for-python](https://github.com/rajiv-thorat/benchmark-for-taint-analysis-tools-for-python) 
by Rajiv Thorat for evaluating various SAST tools. Credit to Rajiv for creating all the tests and meta-data.

This has been simplified to be mainly used with [joern-benchmarks](https://github.com/joernio/joern-benchmarks).

## Tests

The tests themselves can be found under `tests` where the analysis category and test number form the directory name. 
Each directory contains a `Pipfile` and `requirements.txt` to allow for each program to be constructed as an executable 
test case.

Some test cases include benign code to exercise a tools precision against true negatives. These test files are suffixed
to represent this as follows:

* `_actual.py`: A flow exists from a tainted source to sink (true positive/false negative)
* `_sanitize.py`: A flow exists from a tainted source to sink via a sanitizer (false positive/true negative)
* `_false_positive.py`: No flow exists from a tainted source to sink via a sanitizer (false positive/true negative)

## Meta Data

`tests_metadata` mirrors the directories under `tests` and contains various JSON files suffixed similarly to the tests:

* `_actual_taf.json`
* `_sanitized_taf.json`
* `_false_positive_taf.json`

Each will specify the source, sink, and if a flow exists.

Then there is a file suffixed as `_meta-data.json` describing the whole test and various related metrics.
