import ast
from typing import Generator, Tuple, Type, Any, List, Union

import importlib.metadata as importlib_metadata

MSG = 'CLB100 no blank line after the end of an indented block'
BLOCKS_REQUIRING_INDENT = (
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.If,
    ast.With,
    ast.AsyncWith,
    ast.Try,
    ast.ExceptHandler,
)

ModuleLikeTypes = Union[
    ast.Mod, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
]


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def generic_visit(self, node: ModuleLikeTypes) -> None:
        self._check_one_node(node)

    def _check_one_node(self, node) -> None:
        if 'body' in node.__dict__:
            self._check_a_list_of_items(node.body)

        if 'orelse' in node.__dict__:
            self._check_a_list_of_items(node.orelse)

        if 'handlers' in node.__dict__:
            self._check_a_list_of_items(node.handlers)

        if 'finalbody' in node.__dict__:
            self._check_a_list_of_items(node.finalbody)

    def _check_a_list_of_items(self, item_list: list) -> None:
        for i, this_item in enumerate(item_list):
            if isinstance(
                    this_item,
                    (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef),
            ):
                self.generic_visit(this_item)  # as if it were an ast.Module

            if isinstance(this_item, BLOCKS_REQUIRING_INDENT):
                self._check_one_node(this_item)
                if i < len(item_list) - 1:  # not the last item
                    next_item = item_list[i + 1]
                    if (
                            # Because it's OK to have "except ..." right after
                            # the previous line without a blank line
                            not isinstance(next_item, ast.ExceptHandler)
                            and next_item.lineno - this_item.end_lineno <= 1
                    ):
                        line = this_item.end_lineno

                        # Column offset is relative (we need to accumulate it
                        # from the root of the tree), and it doesn't really
                        # provide a lot of valuable information for this
                        # particular style violation, so we use 0 here for now.
                        col = 0
                        self.problems.append((line, col))


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.problems:
            yield line, col, MSG, type(self)
