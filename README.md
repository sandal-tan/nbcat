# `nbcat` - `cat` for Jupyter Notebooks

Display syntax-highlighted, markdown-rendered, jupyter notebooks in your terminal.

Built using [rich](https://github.com/willmcgugan/rich), `nbcat` is capable of displaying a rendered jupyter notebook to your terminal.

[![asciicast](https://asciinema.org/a/328997.svg)](https://asciinema.org/a/328997)

## Usage

Usage is very simple, to `cat` a notebook run:

    $ nbcat <notebook>

## Installation

You can install `nbcat` via:

    $ pip install nbcat

## Development

This project is managed with [poetry](https://python-poetry.org/), to install the development environment:

    $ git clone
    $ cd nbcat
    $ poetry install 


## Future Goals

[ ] Printout cell and notebook metadata
[ ] Natively scroll-able
[ ] Render pandas DataFrames as tables
