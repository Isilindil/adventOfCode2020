#!/usr/bin/python

def create_dict(data) :
    bags_rules = {}
    for rule in data :
        reformated_rule = rule.replace(".", "").replace(" bags", "").replace(" bag", "")
        out_layer, in_bags = reformated_rule.split(" contain ")

        out_layer = out_layer.replace(" ", "")
        bags_rules[out_layer] = []

        in_bags = in_bags.split(", ")
        for bags in in_bags :
            sp = bags.split()
            bags_rules[out_layer].append("".join(sp[1:]))
    return bags_rules

def can_I_contain_gold(bag, start_bag, chain_bags) :
    for nextBag in chain_bags[bag] :
        if nextBag == "shinygold": return True  # can contain a shiny gold bag
        if nextBag == "other": return False  # no bag inside
        if nextBag == start_bag: return False  # cycle is bad
        result = can_I_contain_gold(nextBag, start_bag, chain_bags)
        if result : return True
    return False


if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()

    chain_bags = create_dict(data)
    total_with_shiny = 0

    for outer in chain_bags.keys() :
        result_rules = can_I_contain_gold(outer, outer, chain_bags)
        if result_rules : total_with_shiny += 1

    print(total_with_shiny)
