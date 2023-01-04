import argparse
import ast

class LevenshteinDistance:
    @staticmethod
    def distance(a: str, b: str) -> int:
        """Calculates the Levenshtein distance between a and b."""
        n, m = len(a), len(b)
        if n > m:
            # Make sure n <= m, to use O(min(n, m)) space
            a, b = b, a
            n, m = m, n

        # Keep current and previous row, not entire matrix
        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add = previous_row[j] + 1
                delete = current_row[j - 1] + 1
                change = previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]


class Comparison:
    def __init__(self, input_file: str, output_file: str) -> None:
        self.input_file = input_file
        self.output_file = output_file

    def compare(self) -> None:
        with open(self.input_file, 'r', encoding="utf8") as input_f:
            with open(self.output_file, 'w', encoding="utf8") as output_f:
                # Processing data from input_file and writing results to output_file
                for line in input_f:
                    doc1, doc2 = line.strip().split()
                    # Reading text from doc1 and doc2
                    text1 = self.read_text_from_file(doc1)
                    text2 = self.read_text_from_file(doc2)
                    # Parsing text into an abstract syntax tree and generate a string with code
                    code1_str = ast.unparse(ast.parse(text1))
                    code2_str = ast.unparse(ast.parse(text2))

                    code_str_len = max(len(code1_str), len(code2_str))

                    # Calculation Levenshtein distance between abstract syntax trees and normalization
                    distance = LevenshteinDistance.distance(code1_str, code2_str)
                    distance /= code_str_len
                    # Calculation similarity score
                    score = 1 - distance
                    # Writing similarity score to output_file
                    output_f.write(f"{score:.3f}\n")

    def read_text_from_file(self, file_path: str) -> str:
        with open(file_path, 'r', encoding="utf8") as f:
            return f.read()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    args = parser.parse_args()
    compare = Comparison(args.input_file, args.output_file)
    compare.compare()
