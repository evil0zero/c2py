"""Command line interface for the c2py tool."""

from __future__ import annotations

import argparse
import runpy
from pathlib import Path

import codegen_py
import parser_c
import runtime
import debugger
import benchmark


def translate_command(args: argparse.Namespace) -> None:
    """Translate C source code to Python source code."""
    source = Path(args.source).read_text()
    ast = parser_c.parse_c_code(source)
    py_code = codegen_py.generate_py_code(ast)
    if args.output:
        Path(args.output).write_text(py_code)
    else:
        print(py_code)


def run_command(args: argparse.Namespace) -> None:
    """Translate and run the provided C source code."""
    source = Path(args.source).read_text()
    ast = parser_c.parse_c_code(source)
    py_code = codegen_py.generate_py_code(ast)
    exec(py_code, {"runtime": runtime})


def debug_command(args: argparse.Namespace) -> None:
    """Run the translated code under the debugger."""
    source = Path(args.source).read_text()
    ast = parser_c.parse_c_code(source)
    py_code = codegen_py.generate_py_code(ast)
    debugger.debug_code(py_code, {"runtime": runtime})


def bench_command(args: argparse.Namespace) -> None:
    """Benchmark C vs translated Python code."""
    benchmark.benchmark(args.source)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="c2py", description="Translate C/C++ code to Python")
    subparsers = parser.add_subparsers(dest="command", required=True)

    trans_p = subparsers.add_parser("translate", help="Translate C/C++ to Python")
    trans_p.add_argument("source", help="Input source file")
    trans_p.add_argument("--output", help="Output Python file")
    trans_p.set_defaults(func=translate_command)

    run_p = subparsers.add_parser("run", help="Run translated C/C++ code")
    run_p.add_argument("source", help="Input source file")
    run_p.set_defaults(func=run_command)

    dbg_p = subparsers.add_parser("debug", help="Run under debugger")
    dbg_p.add_argument("source", help="Input source file")
    dbg_p.set_defaults(func=debug_command)

    bench_p = subparsers.add_parser("bench", help="Benchmark C vs Python")
    bench_p.add_argument("source", help="Input source file")
    bench_p.set_defaults(func=bench_command)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
