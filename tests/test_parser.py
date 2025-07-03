"""Tests for the parser."""

from __future__ import annotations

import parser_c


def test_parse_simple_c():
    code = "int main() { return 0; }"
    ast = parser_c.parse_c_code(code)
    assert ast is not None
