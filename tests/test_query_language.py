import pytest

from galois.query_language import Node, parse


# unit test to assert that the parse function returns the correct AST in Node class with OR AND and NOT operators
def test_parse():
    query = "(AND (OR field1>value1 field2<value2) (NOT field3=value3))"
    expected = Node(
        "AND",
        [
            Node(
                "OR",
                [
                    Node(
                        ">",
                        [Node("field", value="field1"), Node("value", value="value1")],
                    ),
                    Node(
                        "<",
                        [Node("field", value="field2"), Node("value", value="value2")],
                    ),
                ],
            ),
            Node(
                "NOT",
                [
                    Node(
                        "=",
                        [Node("field", value="field3"), Node("value", value="value3")],
                    )
                ],
            ),
        ],
    )

    node = parse(query)

    def assert_node(node, expected):
        assert node.type == expected.type
        assert node.value == expected.value
        for i in range(len(node.children)):
            assert_node(node.children[i], expected.children[i])

    assert_node(node, expected)
