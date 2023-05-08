import pytest

from galois.query_language import Node, parse, evaluate


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


def test_evaluate():
    # Test data
    data = {"x": 5, "y": 3}

    # Test AND
    and_node = Node(
        "AND",
        [
            Node("<", [Node("field", value="x"), Node("value", value=10)]),
            Node(">", [Node("field", value="y"), Node("value", value=1)]),
        ],
    )
    assert evaluate(and_node, data) == True

    # Test OR
    or_node = Node(
        "OR",
        [
            Node("<", [Node("field", value="x"), Node("value", value=3)]),
            Node(">", [Node("field", value="y"), Node("value", value=1)]),
        ],
    )
    assert evaluate(or_node, data) == True

    # Test NOT
    not_node = Node(
        "NOT", [Node("<", [Node("field", value="x"), Node("value", value=3)])]
    )
    assert evaluate(not_node, data) == True

    # Test <
    lt_node = Node("<", [Node("field", value="x"), Node("value", value=10)])
    assert evaluate(lt_node, data) == True

    # Test >
    gt_node = Node(">", [Node("field", value="y"), Node("value", value=1)])
    assert evaluate(gt_node, data) == True

    # Test =
    eq_node = Node("=", [Node("field", value="x"), Node("value", value=5)])
    assert evaluate(eq_node, data) == True

    # Test invalid node type
    invalid_node = Node("INVALID")
    try:
        evaluate(invalid_node, data)
        assert False, "Should have raised an exception"
    except Exception as e:
        assert str(e) == "Invalid node type 'INVALID'"
