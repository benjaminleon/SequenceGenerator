class SequenceGenerator:
    """Generates a sequence of numbers which contains all the possible combinations of 4-digit key codes"""

    def __init__(self):
        self.codes = []
        for x in range(10000):
            code = str(x)
            while len(code) < 4:
                code = "0" + code

            self.codes.append(code)

        self.sequence = []

    def generate(self):
        code = self.codes[0]
        self.sequence = code
        self.codes.remove(code)

        while not self.codes == []:
            code = self.codes[0]
            for number in code:
                self.sequence += number
                if self.sequence[-4:] in self.codes:
                    self.codes.remove(self.sequence[-4:])

            if code in self.codes:
                self.codes.remove(code)


if __name__ == "__main__":
    generator = SequenceGenerator()
    generator.generate()
    print("Length of the sequence: " + str(len(generator.sequence)))
    print(generator.sequence)
