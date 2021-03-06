from __future__ import print_function
import sys

import click

import truthtable
import normal_forms
import proofs

@click.group()
def cli():
    """Carroll is a command line tool for analysing propositional logic (also known as boolean functions or expressions).
    """
    pass

@cli.command()
@click.argument("expression_1")
@click.argument("expression_2")
def equiv(expression_1, expression_2):
    """Checks whether two expressions are logically equivalent."""
    print(truthtable.equivalent(expression_1, expression_2))

@cli.command()
@click.argument("expression")
@click.option("--verbose", is_flag=True, default=False, help="Check for satisfiability, validity etc.")
def table(expression, verbose):
    """Outputs a truth table for a logical expression."""
    truthtable.print_truth_table(expression, verbose)

@cli.command()
@click.argument("expression")
def dnf(expression):
    """Converts an expression to disjunctive normal form."""
    print(normal_forms.to_dnf(expression))

@cli.command()
@click.argument("expression")
def cnf(expression):
    """Converts an expression to conjunctive normal form."""
    print(normal_forms.to_cnf(expression))

@cli.command()
def proof():
    """Checks a proof for validity."""
    exp = raw_input()
    expressions = []
    while exp:
        expressions.append(exp)
        exp = raw_input()
    if proofs.valid_proof(expressions):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    cli()
