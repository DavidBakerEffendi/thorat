from os import listdir
from os.path import join
import json

tests_metadata = 'tests_metadata'
# Keys
actual_flow = 'Actual Flow'
no_flow = 'No Flow'
san_flow = 'Sanitized Flow'

if __name__ == "__main__":
    print("[i] Summarizing Tests")
    results_table = {}
    for test_meta in listdir(tests_metadata):
        last_underscore_idx = test_meta.rfind('_')
        test_category = test_meta[:last_underscore_idx]
        meta_files = listdir(join(tests_metadata, test_meta))
        tn_count = len(list(filter(lambda f: f.endswith('_false_positive_taf.json'), meta_files)))
        tp_count = len(list(filter(lambda f: f.endswith('_actual_taf.json'), meta_files)))
        san_count = len(list(filter(lambda f: f.endswith('_sanitized_taf.json'), meta_files)))

        if test_category not in results_table.keys():
            results_table[test_category] = {no_flow: 0, san_flow: 0, actual_flow: 0}

        results_table[test_category][no_flow] += tn_count
        results_table[test_category][actual_flow] += tp_count
        results_table[test_category][san_flow] += san_count

    print("[i] Writing summary to `tests_summary.json`")
    with open('tests_summary.json', 'w') as f:
        json.dump(results_table, f, sort_keys=True, indent=2)

    print("[i] Writing MKD Table to stdout")

    print(f"|Category|{actual_flow}|{no_flow}|{san_flow}|Total|")
    print(f"|---|---|---|---|---|")
    grand_total = 0
    for (k, v) in results_table.items():
        total = v[actual_flow] + v[no_flow] + v[san_flow]
        grand_total += total
        print(f"|{k}|{v[actual_flow]}|{v[no_flow]}|{v[san_flow]}|{total}|")
    print(f"|Grand Total| | | |{grand_total}|")
