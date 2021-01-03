#!/usr/bin/python

def parse_allow_range(category_list):
    all_range_per_category = {}
    for line in category_list:
        cat, allow_range = line.split(":")
        allow_range = allow_range.split("or")
        down1, up1 = allow_range[0].split("-")
        down2, up2 = allow_range[1].split("-")
        if cat not in all_range_per_category:
            all_range_per_category[cat] = [(int(down1), int(up1)), (int(down2), int(up2))]
        else:
            print(f"category {cat} present 2 times")
    return all_range_per_category


def check_tickets(near_tickets, allow_range):
    wrong_values = []
    for ticket in near_tickets:
        all_values = [int(val) for val in ticket.split(",")]
        for value in all_values:
            wrong = True
            for k, v in allow_range:
                for down, up in v:
                    if down < value < up:
                        print("ok")
            if wrong:
                wrong_values.append(value)
    return wrong_values


if __name__ == "__main__":
    with open("input_nearby_tickets") as a:
        near_ticket = a.read().split("\n")
    a.close()
    with open("input_your_ticket") as a:
        your_ticket = a.read().split("\n")
    a.close()
    with open("input_categories") as a:
        categories = a.read().split("\n")
    a.close()
    print(near_ticket)
    print(your_ticket)
    print(categories)

    range_of_category = parse_allow_range(categories)

    check_tickets(near_ticket, range_of_category)
