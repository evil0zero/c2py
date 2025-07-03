"""Benchmark C execution vs translated Python code."""

from __future__ import annotations

import os
import subprocess
import tempfile
import time
from pathlib import Path

import parser_c
import codegen_py
import runtime


def compile_c(source_file: str, output: str) -> None:
    subprocess.check_call(["gcc", "-O2", source_file, "-o", output])


def benchmark(source_file: str) -> None:
    """Run the benchmark and print timing information."""
    with tempfile.TemporaryDirectory() as tmpdir:
        binary = os.path.join(tmpdir, "a.out")
        compile_c(source_file, binary)
        start = time.perf_counter()
        subprocess.check_call([binary])
        c_time = time.perf_counter() - start

        source = Path(source_file).read_text()
        ast = parser_c.parse_c_code(source)
        py_code = codegen_py.generate_py_code(ast)
        start = time.perf_counter()
        runtime.execute(py_code)
        py_time = time.perf_counter() - start

    print(f"C time: {c_time:.6f}s")
    print(f"Python time: {py_time:.6f}s")
