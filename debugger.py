"""Simple debugging utilities using pdb."""

from __future__ import annotations

import pdb


def debug_code(code: str, globals_dict: dict[str, object] | None = None) -> None:
    """Run the provided code under pdb."""
    pdb.run(code, globals_dict if globals_dict is not None else {})
