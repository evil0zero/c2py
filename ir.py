"""Intermediate representation of parsed C/C++ code."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List


@dataclass
class Function:
    """Represents a C/C++ function."""

    name: str
    body: Any


@dataclass
class Program:
    """Represents an entire program."""

    functions: List[Function]
