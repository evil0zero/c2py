"""Simple runtime environment to simulate C memory."""

from __future__ import annotations


class Memory:
    """A naive memory manager using Python bytearrays."""

    def __init__(self) -> None:
        self._storage: dict[int, bytearray] = {}
        self._next_addr = 1

    def malloc(self, size: int) -> int:
        addr = self._next_addr
        self._storage[addr] = bytearray(size)
        self._next_addr += size
        return addr

    def free(self, addr: int) -> None:
        self._storage.pop(addr, None)

    def read(self, addr: int, size: int) -> bytes:
        data = self._storage.get(addr)
        if data is None:
            raise ValueError("Invalid address")
        return bytes(data[:size])

    def write(self, addr: int, data: bytes) -> None:
        buf = self._storage.get(addr)
        if buf is None:
            raise ValueError("Invalid address")
        buf[: len(data)] = data


def execute(code: str) -> None:
    """Execute translated Python code inside a fresh globals dict."""
    env = {"memory": Memory()}
    exec(code, env)
