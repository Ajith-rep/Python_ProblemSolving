class StringSeperator:
    def __init__(self, string):
        self.string = string

    def seperate(self):
        alpha = ""
        num = ""
        spec = ""
        for s in self.string:
            if s.isalpha():
                alpha += s
            elif s.isdigit():
                num += s
            else:
                spec += s

        print(
            f"Given String After Seperation:\n Numbers: {num}\n Alphabets: {alpha} \n Special Symbols: {spec}"
        )

s1 = StringSeperator("Ajith89324$%&$^()")
s1.seperate()