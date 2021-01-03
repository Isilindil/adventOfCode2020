#!/usr/bin/python

if __name__ == "__main__":
    with open("input_nerby_tickets") as a:
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

