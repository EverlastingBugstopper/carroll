import truthtable
import parser
from nose.tools import assert_equals

def to_dnf(expression):
    """Converts a proposition string into a DNF string."""
    table = truthtable.truth_table(expression)
    output = "("
    for row in table:
        if row.value:
            output += "(%s) v " % model_to_and_clause(row.model)
    output = output[:-3] + ")"
    return output

def model_to_and_clause(model):
    l = []
    for atom, truth in model.items():
        if truth:
            l.append((atom, atom))
        else:
            l.append((atom, "~"+atom))
    l.sort()
    return " & ".join([elem[1] for elem in l])

def test_basic_dnf():
    expression = "(A & (B | C))"
    expected = "((A & B & C) v (A & B & ~C) v (A & ~B & C))"
    actual = to_dnf(expression)
    assert_equals(expected, actual)

