# scope_examples.py — Simple scope examples

# Local scope
def show_local():
    x = "Local"
    print("Local:", x)

x = "Global1"
show_local()
print("Outside:", x)


# Enclosing scope
def outer():
    y = "Outer"

    def inner():
        y = "Inner"
        print("Inner:", y)

    inner()
    print("Outer:", y)

y = "Global2" # Global
outer()
print("Global:", y)


# nonlocal example
def demo_nonlocal():
    z = "Old"

    def change():
        nonlocal z
        z = "New"

    change()
    print("Nonlocal:", z)

demo_nonlocal()


# global example
status = "Start"

def update_global():
    def modify():
        global status
        status = "Updated"
    modify()

update_global()
print("Global:", status)
