from collections import defaultdict

from .base import BaseDailySolution


def is_valid_rule(rule: list[str], graph_edges: dict[str, set[str]]) -> bool:
    for i in range(len(rule) - 1):
        if not all(entry in graph_edges[rule[i]] for entry in rule[i + 1 :]):
            return False
    return True


def make_valid_rule(rule: list[str], graph_edges: dict[str, set[str]]) -> list[str]:
    new_rule: list[str] = []
    while len(rule) > 0:
        rule_set = set(rule)
        for entry in rule:
            rule_set.discard(entry)
            if all(elt in graph_edges[entry] for elt in rule_set):
                new_rule.append(entry)
                rule = list(rule_set)
                break
            else:
                rule_set.add(entry)

    return new_rule


class Day5Solution(BaseDailySolution):
    DAY = 5

    @classmethod
    def format_data(
        cls, input_data: list[str]
    ) -> tuple[dict[str, set[str]], list[list[str]]]:
        graph_edges: dict[str, set[str]] = defaultdict(set)
        rules: list[list[str]] = []

        for entry in input_data:
            if "|" in entry:
                edge1, edge2 = entry.strip().split("|")
                graph_edges[edge1].add(edge2)
            elif "," in entry:
                rules.append([e.strip() for e in entry.strip().split(",")])

        return graph_edges, rules

    @classmethod
    def solve_part_1(
        cls, input_data: tuple[dict[str, set[str]], list[list[str]]]
    ) -> int:
        """

        :param input_data:
        :return:
        """
        graph_edges, rules = input_data
        total = 0

        for rule in rules:
            if is_valid_rule(rule, graph_edges):
                total += int(rule[int(len(rule) / 2)])
        return total

    @classmethod
    def solve_part_2(
        cls, input_data: tuple[dict[str, set[str]], list[list[str]]]
    ) -> int:
        """
        Find the updates which are not in the correct order. What do you get if you add up the middle page numbers
        after correctly ordering just those updates.

        :param input_data:
        :return:
        """
        graph_edges, rules = input_data
        total = 0

        for rule in rules:
            if not is_valid_rule(rule, graph_edges):
                new_rule = make_valid_rule(rule, graph_edges)
                total += int(new_rule[int(len(new_rule) / 2)])
        return total
