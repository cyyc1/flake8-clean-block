from __future__ import annotations

import os
import ast
import sys
import pytest
from typing import Set

from flake8_clean_block import Plugin

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(THIS_DIR)

import ok_cases
import not_ok_cases


def _results(src_code: str) -> Set[str]:
    tree = ast.parse(src_code)
    plugin = Plugin(tree)
    return {
        f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()
    }


@pytest.mark.parametrize('src_code', ok_cases.collect_all_cases())
def test_ok_cases(src_code):
    assert _results(src_code) == set()


@pytest.mark.parametrize('src_code,lines', not_ok_cases.collect_all_cases())
def test_no_ok_cases(src_code, lines):
    expected_violation_messages = {
        f'{line}:0 CLB100 no blank line after the end of an indented block'
        for line in lines
    }
    assert _results(src_code) == expected_violation_messages
