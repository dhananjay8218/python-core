# generators_basic.py — Generator examples
# A generator is a function that produces values one at a time using 'yield'.

# Basic generator
def item_stream():
    yield "Item 1"
    yield "Item 2"
    yield "Item 3"

stream = item_stream()

# for item in stream:
#     print(item)

print(next(stream))
print(next(stream))
print(next(stream))


# Generator vs normal list function
def get_list():
    return ["A", "B", "C"]

def get_gen():
    yield "A"
    yield "B"
    yield "C"

g = get_gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  gives error


# Infinite generator
def counter():
    num = 1
    while True:
        yield f"Count {num}"
        num += 1

c1 = counter()
c2 = counter()

for _ in range(5):
    print(next(c1))

for _ in range(6):
    print(next(c2))


# Generator with send()
def responder():
    print("Ready for input...")
    value = yield  # First yield pauses and waits for the first .send()

    while True:
        print("Received:", value)
        # This yield pauses again and waits for the next .send() value
        value = yield

r = responder()
next(r)          # Start the generator, run until first yield
r.send("Hello")  # Sends "Hello" to the generator
r.send("World")  # Sends "World" to the generator



# yield from example
def local_items():
    yield "A1"
    yield "A2"

def external_items():
    yield "B1"
    yield "B2"

def full_list():
    yield from local_items()
    yield from external_items()

for x in full_list():
    print(x)


# Handling close()
def session():
    try:
        while True:
            msg = yield "Waiting"
    except GeneratorExit:
        print("Session closed")

s = session()
print(next(s))
s.close() #cleanup memory