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

## Summary

`metrics.py` will generate a simple summary as below, including a JSON readable variant `tests_summary.json`.

|Category|Actual Flow|No Flow|Sanitized Flow|Total|
|---|---|---|---|---|
|dict_access|1|1|1|3|
|lambda_functions|2|0|0|2|
|with_statement|3|0|3|6|
|for_statement|1|1|1|3|
|while_statement|1|1|1|3|
|decorator|2|0|0|2|
|function_call|2|0|1|3|
|field_sensitivity|2|3|3|8|
|list_access|2|1|0|3|
|deque_access|1|1|1|3|
|list_to_string|1|0|0|1|
|static_functions|1|0|0|1|
|imports|1|0|0|1|
|threading|1|1|0|2|
|inherited_objects|1|1|0|2|
|exceptions|3|2|0|5|
|serialization|1|0|0|1|
|object_sensitivity|1|1|1|3|
|minimal_test|2|1|0|3|
|aliasing|1|1|0|2|
|match_statement|0|0|0|0|
|exec|1|0|0|1|
|deque_clone|1|0|0|1|
|if_statement|1|1|1|3|
|multi_dementional_array|1|1|0|2|
|structural_subtypting|1|1|0|2|
|abstract_factory|1|0|1|2|
|reflection|3|0|0|3|
|recursion|1|0|0|1|
|list_copy|1|1|0|2|
|Grand Total| | | |74|
