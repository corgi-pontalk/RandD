# generate_file.py
import datetime

def main():
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"generated_{now}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Hello! This file was generated at {now}\n")
    print(f"Created file: {filename}")

if __name__ == "__main__":
    main()

