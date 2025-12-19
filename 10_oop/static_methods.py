# staticmethod_example.py — Static method example

class Utils:
    @staticmethod
    def clean_list(text):
        return [item.strip() for item in text.split(",")]

raw = " a , b , c , d "
cleaned = Utils.clean_list(raw)
print(cleaned)
