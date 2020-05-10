"""Notebook data model."""

from dataclasses import dataclass, field
import typing as T

from rich.console import Console
from rich.rule import Rule
from rich.markdown import Markdown
from rich.syntax import Syntax


@dataclass
class Cell:
    """Base model of a notebook cell."""

    cell_type: str
    metadata: T.Dict  = field(default_factory=dict)
    execution_count: int = field(default=0)
    source: T.List[str] = field(default_factory=list)
    outputs: T.List[T.Dict] = field(default_factory=list)

    def render(self, console: Console):
        """Render a cell to a console."""
        raise NotImplementedError("Render must be overridden.")

class MarkdownCell(Cell):

    def render(self, console: Console):
        console.print('\n', Markdown(''.join(self.source)))

class CodeCell(Cell):

    def render(self, console: Console):
        console.print(
            f'\n -> {self.execution_count}',
            Syntax(''.join(self.source), 'python', line_numbers=True, highlight_lines=False),
        )
        if self.outputs:
            console.print(
                Rule(character='-'),
                *self.outputs[0]['text']
                # Syntax(''.join(f'>>> {loc}' for loc in self.outputs[0]['text']), 'python'),
            )
        console.print(Rule())

def make_cell(**cell_kwargs) -> Cell:
    """Make a typed cell."""
    cell_type = cell_kwargs.get('cell_type')
    if cell_type is None:
        return None
    if cell_type == 'markdown':
        return MarkdownCell(**cell_kwargs)
    if cell_type == 'code':
        return CodeCell(**cell_kwargs)

@dataclass
class Notebook:

    nbformat: int
    nbformat_minor: int
    metadata: T.Dict = field(default_factory=dict)
    cells: T.List[Cell] = field(default_factory=list)

    def __post_init__(self):
        renderable_cells = []
        for cell in self.cells:
            renderable_cells.append(make_cell(**cell))
        self.cells = renderable_cells

    def render(self, console: Console):
        for cell in self.cells:
            if cell:
                cell.render(console)
