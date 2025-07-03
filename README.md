# c2py

`c2py` is a prototype tool that translates small fragments of C or C++ code
into Python. The goal is to enable rapid experimentation with C code without
invoking a full compiler.

## Features

- Parsing of C code using `pycparser`.
- Optional C++ parsing when Clang bindings are available.
- Generation of placeholder Python code from the parsed representation.
- A simple runtime system that simulates C-style memory management.
- Command line interface with subcommands to translate, run, debug and
  benchmark code.

## Limitations

This project is an early prototype. The Python code generation only produces a
stub function and does not yet emulate complex semantics. C++ translation is
only supported when the `clang` Python package is installed.

## Development

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
pytest -q
```
