import re
from dataclasses import dataclass, field


class Node:
    def __init__(self, type: str, children: list["Node"] = [], value=None):
        self.type = type
        self.children = children
        self.value = value


def parse(query: str) -> Node:
    """Parse a query string into an AST."""
    valid_operators = ["AND", "OR", "NOT", "=", "<", ">"]
    tokens = query.split()

    def parse_expression(index) -> tuple[Node, int]:
        token = tokens[index]
        if token == "(":
            operator = tokens[index + 1]
            if operator not in valid_operators:
                raise Exception(f"Invalid operator '{operator}'")
            index += 2
            children = []
            while tokens[index] != ")":
                child, index = parse_expression(index)
                children.append(child)
            if len(children) == 0:
                raise Exception("Empty expression after logical operator")
            return Node(operator, children), index + 1
        else:
            match = re.match(r"([a-zA-Z0-9]+)([<>=])([a-zA-Z0-9]+)", token)
            if match:
                field, operator, value = match.groups()
                if operator in valid_operators:
                    return (
                        Node(
                            operator,
                            [Node("field", value=field), Node("value", value=value)],
                        ),
                        index + 1,
                    )
                else:
                    raise Exception(f"Invalid operator '{operator}'")
            else:
                raise Exception(f"Invalid token '{token}'")

    return parse_expression(0)[0]
