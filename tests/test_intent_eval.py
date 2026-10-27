"""Ensure reporting cannot hide missing cases, critical failures or UI-only gains."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('intent_eval', Path(__file__).resolve().parents[1] / 'scripts/summarize_intent_eval.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ReportingTests(unittest.TestCase):
    def setUp(self):
        self.cases = [{'id': 'core', 'stratum': 'core'}, {'id': 'ui', 'stratum': 'ui'}]
        self.rows = [{'id': c['id'], 'variant': variant, 'verdict': 'pass', 'critical_errors': [],
                      'response': 'Actual output', 'rationale': 'Reviewed against the case'}
                     for c in self.cases for variant in ('baseline', 'candidate')]

    def test_missing_or_duplicate_observations_are_rejected(self):
        with self.assertRaises(ValueError):
            m.summarize(self.cases, self.rows[:-1])
        with self.assertRaises(ValueError):
            m.summarize(self.cases, self.rows + [self.rows[0]])

    def test_ui_improvement_is_not_core_improvement(self):
        self.rows[2]['verdict'] = 'fail'
        result = m.summarize(self.cases, self.rows, 1)
        self.assertEqual(result['slices']['ui']['recoveries'], ['ui'])
        self.assertEqual(result['practical_gate'], 'inconclusive-insufficient-core-gain')

    def test_critical_failure_cannot_be_hidden_by_pass(self):
        self.rows[1]['critical_errors'] = ['Changed an exact constraint']
        with self.assertRaises(ValueError):
            m.summarize(self.cases, self.rows)
        self.rows[1]['verdict'] = 'fail'
        self.assertEqual(m.summarize(self.cases, self.rows)['practical_gate'], 'not-met-regression-or-critical-error')

    def test_unknown_is_not_counted_as_improvement(self):
        self.rows[0]['verdict'] = 'unknown'
        result = m.summarize(self.cases, self.rows, 1)
        self.assertEqual(result['slices']['core']['recoveries'], [])
        self.assertEqual(result['practical_gate'], 'inconclusive-missing-judgment')

    def test_core_gain_requires_no_regression_in_either_stratum(self):
        self.rows[0]['verdict'] = 'fail'
        self.assertEqual(m.summarize(self.cases, self.rows, 1)['practical_gate'], 'met-on-this-case-set')
        self.rows[3]['verdict'] = 'fail'
        self.assertEqual(m.summarize(self.cases, self.rows, 1)['practical_gate'], 'not-met-regression-or-critical-error')

    def test_stable_failure_and_baseline_critical_remain_visible(self):
        self.rows[0]['verdict'] = self.rows[1]['verdict'] = 'fail'
        self.rows[0]['critical_errors'] = ['Invented an unavailable fact']
        result = m.summarize(self.cases, self.rows)
        self.assertEqual(result['slices']['core']['stable_failures'], ['core'])
        self.assertEqual(result['slices']['core']['baseline_critical'], ['core'])
        self.assertEqual(result['slices']['ui']['stable_passes'], ['ui'])


if __name__ == '__main__':
    unittest.main()
