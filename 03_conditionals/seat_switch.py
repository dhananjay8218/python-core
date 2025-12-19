# seat_switch.py — Match-case example

# seat = input("Enter seat type (sleeper/ac/general/luxury): ").lower()
#
# match seat:
#     case "sleeper":
#         print("Sleeper — Bed, no AC")
#     case "ac":
#         print("AC — Air conditioned")
#     case "general":
#         print("General — Basic seating")
#     case "luxury":
#         print("Luxury — Premium seating")
#     case _:
#         print("Invalid seat type")


# seat_switch_dict.py

seat = input("Enter seat type: ").lower()

options = {
    "sleeper": "Sleeper — Bed, no AC",
    "ac": "AC — Air conditioned",
    "general": "General — Basic seating",
    "luxury": "Luxury — Premium seating"
}

print(options.get(seat, "Invalid seat type"))
