#!/usr/bin/env python3
"""Aggregate supplied paired judgments; no model calls or automatic semantic grading."""
import argparse
import json
from pathlib import Path


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]


def summarize(cases, results, minimum_recoveries=4):
    if minimum_recoveries < 1:
        raise ValueError('minimum_recoveries must be positive')
    indexed = {}
    for case in cases:
        key = case['id']
        if key in indexed or case['stratum'] not in {'core', 'ui'}:
            raise ValueError('Duplicate case or unknown stratum: ' + key)
        indexed[key] = case
    if not indexed or not any(c['stratum'] == 'core' for c in cases):
        raise ValueError('A nonempty core case set is required')
    observations = {}
    for row in results:
        key = (row['id'], row['variant'])
        if key in observations or key[0] not in indexed or key[1] not in {'baseline', 'candidate'}:
            raise ValueError('Duplicate or unexpected observation: ' + str(key))
        if row['verdict'] not in {'pass', 'fail', 'unknown'}:
            raise ValueError('Invalid verdict: ' + str(key))
        if not isinstance(row['critical_errors'], list) or not all(isinstance(x, str) and x for x in row['critical_errors']):
            raise ValueError('critical_errors must be a list of explanations')
        if row['verdict'] == 'pass' and row['critical_errors']:
            raise ValueError('A critical violation cannot be averaged into a pass')
        if not isinstance(row['response'], str) or not row['response'].strip() or not isinstance(row['rationale'], str) or not row['rationale'].strip():
            raise ValueError('Actual response and review rationale are required')
        observations[key] = row
    expected = {(key, variant) for key in indexed for variant in ('baseline', 'candidate')}
    if set(observations) != expected:
        raise ValueError('Incomplete paired results; do not silently drop missing cases')
    def count(ids):
        stats = {'cases': len(ids), 'baseline_passes': 0, 'candidate_passes': 0,
                 'recoveries': [], 'regressions': [], 'stable_passes': [], 'stable_failures': [],
                 'unknown': [], 'baseline_critical': [], 'candidate_critical': [],
                 'baseline_failed': [], 'candidate_failed': []}
        for key in ids:
            before = observations[(key, 'baseline')]
            after = observations[(key, 'candidate')]
            stats['baseline_passes'] += before['verdict'] == 'pass'
            stats['candidate_passes'] += after['verdict'] == 'pass'
            if before['verdict'] == 'fail':
                stats['baseline_failed'].append(key)
            if after['verdict'] == 'fail':
                stats['candidate_failed'].append(key)
            if 'unknown' in {before['verdict'], after['verdict']}:
                stats['unknown'].append(key)
            elif before['verdict'] == 'fail' and after['verdict'] == 'pass':
                stats['recoveries'].append(key)
            elif before['verdict'] == 'pass' and after['verdict'] == 'fail':
                stats['regressions'].append(key)
            elif before['verdict'] == after['verdict'] == 'pass':
                stats['stable_passes'].append(key)
            elif before['verdict'] == after['verdict'] == 'fail':
                stats['stable_failures'].append(key)
            if before['critical_errors']:
                stats['baseline_critical'].append(key)
            if after['critical_errors']:
                stats['candidate_critical'].append(key)
        return stats
    slices = {stratum: count([key for key, case in indexed.items() if case['stratum'] == stratum])
              for stratum in ('core', 'ui')}
    categories = {category: count([key for key, case in indexed.items()
                                  if case['stratum'] == 'core' and case.get('category', 'unspecified') == category])
                  for category in sorted({case.get('category', 'unspecified') for case in cases if case['stratum'] == 'core'})}
    core = slices['core']
    if any(s['unknown'] for s in slices.values()):
        gate = 'inconclusive-missing-judgment'
    elif any(s['regressions'] or s['candidate_critical'] for s in slices.values()):
        gate = 'not-met-regression-or-critical-error'
    elif len(core['recoveries']) >= minimum_recoveries:
        gate = 'met-on-this-case-set'
    else:
        gate = 'inconclusive-insufficient-core-gain'
    return {'slices': slices, 'core_categories': categories, 'practical_gate': gate, 'minimum_core_recoveries': minimum_recoveries,
            'scope': 'Supplied reviewer judgments on this fixed case set; not statistical certification, native discovery, or a cross-model accuracy claim.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', required=True)
    parser.add_argument('--results', required=True)
    parser.add_argument('--minimum-recoveries', type=int, default=4)
    parser.add_argument('--output', help='New report file; existing evidence is never overwritten')
    args = parser.parse_args()
    report = summarize(read_jsonl(args.cases), read_jsonl(args.results), args.minimum_recoveries)
    text = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        with Path(args.output).open('x', encoding='utf-8') as handle:
            handle.write(text)
    print(text, end='')


if __name__ == '__main__':
    main()
