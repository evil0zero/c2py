"""Tests for runtime memory management."""

from __future__ import annotations

import runtime


def test_memory_allocation():
    mem = runtime.Memory()
    addr = mem.malloc(4)
    mem.write(addr, b"test")
    data = mem.read(addr, 4)
    assert data == b"test"
    mem.free(addr)
