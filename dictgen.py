import sys
import re
import sre_yield

class DictionaryGenerator:
    output_filename = ""
    password_pattern = ""

    def __init__(self):
        self.output_filename = ""
        self.password_pattern = ""

    @staticmethod
    def show_help():
        print(r"""Usage:
              --help - shows this help.
              -f=[file] - filename to create the dictionary to.
              -p=[PATTERN] - regex pattern to use for dictionary generation.
              """)

    def parse_args(self):
        for arg in sys.argv:
            if arg == "--help":
                self.show_help()
            elif arg.startswith("-p="):
                self.password_pattern = arg[3:]
            elif arg.startswith("-f="):
                self.output_filename = arg[3:]

    def generate_by_pattern(self, pattern):
        return set(sre_yield.AllStrings(pattern))

    def run(self):
        self.parse_args()
        if "--help" not in sys.argv:
            print("Working with pattern:" + self.password_pattern + "\nOutput file: " + self.output_filename + "\n")
            result = self.generate_by_pattern(self.password_pattern)
            for item in sorted(list(result)):
                print(item) # TODO: write to file
                f = open(self.output_filename, "a+")
                f.write(item + "\n")
            f.close()

dictgen = DictionaryGenerator()
dictgen.run()

