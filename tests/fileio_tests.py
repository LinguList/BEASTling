# coding: utf8
from __future__ import unicode_literals, print_function
from unittest import TestCase

from beastling.fileio.datareaders import load_data
from .util import data_path


class Tests(TestCase):
    def test_load_data(self):
        for p in data_path().iterdir():
            if p.suffix == '.csv':
                if p.stem in ['duplicated_iso', 'no_iso', 'nonstandard_lang_col']:
                    self.assertRaises(ValueError, load_data, p)
                else:
                    data = load_data(p)
                    self.assertNotEqual(len(data), 0)

    def test(self):
        beastling_format = load_data(data_path("basic.csv"))
        cldf_format = load_data(data_path("cldf.csv"))
        explicit_cldf_format = load_data(data_path("cldf.csv"),
                                file_format='cldf')
        tabbed_cldf_format = load_data(data_path("cldf.tsv"))
        tabbed_explicit_cldf_format = load_data(data_path("cldf.tsv"),
                                                file_format='cldf')
        assert set(list(beastling_format.keys())) == set(list(cldf_format.keys()))
        assert set(list(beastling_format.keys())) == set(list(explicit_cldf_format.keys()))
        assert set(list(beastling_format.keys())) == set(list(tabbed_cldf_format.keys()))
        assert set(list(beastling_format.keys())) == set(list(tabbed_explicit_cldf_format.keys()))
        for key in beastling_format:
            self.assertEqual(
                set(beastling_format[key].items()), set(cldf_format[key].items()))
            self.assertEqual(
                set(beastling_format[key].items()), set(explicit_cldf_format[key].items()))
            self.assertEqual(
                set(beastling_format[key].items()), set(tabbed_cldf_format[key].items()))
            self.assertEqual(
                set(beastling_format[key].items()), set(tabbed_explicit_cldf_format[key].items()))
