import parser
import os

def test_complex_parser():
    if not os.path.exists("complex_paper.pdf"):
        print("complex_paper.pdf not found.")
        return

    with open("complex_paper.pdf", "rb") as f:
        data = parser.parse_pdf(f)
    
    print("Extracted Data Keys:", data.keys())
    for key, value in data.items():
        print(f"\n--- {key} ---")
        print(value)

if __name__ == "__main__":
    test_complex_parser()
