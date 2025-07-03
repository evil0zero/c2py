"""C/C++ parser using pycparser and clang."""

from __future__ import annotations

from typing import Any

from pycparser import c_parser
try:
    from clang import cindex
except Exception:  # pragma: no cover - clang may not be installed
    cindex = None


_c_parser = c_parser.CParser()


def parse_c_code(source: str) -> Any:
    """Parse C99 source code and return an AST."""
    return _c_parser.parse(source)


def parse_cpp_code(source: str) -> Any:
    """Parse C++ source code using clang if available."""
    if cindex is None:
        raise RuntimeError("clang Python bindings not installed")
    index = cindex.Index.create()
    translation_unit = index.parse("tmp.cpp", unsaved_files=[("tmp.cpp", source)])
    return translation_unit
