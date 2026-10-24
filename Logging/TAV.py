import logging
from pathlib import Path
logging.basicConfig(
    level=logging.INFO,
    filename="file.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EmptyDocumentError(Exception):
    pass

file = Path("file.txt")

logging.info("Application started succesfully")
try:
    with open(file, "r", encoding="utf-8") as f:
        logging.info("File opened successfull")
        content = f.read()
        if not content.strip():
            raise EmptyDocumentError("Empty File")
except FileNotFoundError:
    logging.error("file not found")
    print("File not Found")
    
except EmptyDocumentError:
    logging.error("empty file")
    print("File has no content ")

count_lines = len(content.splitlines())
print("Total Lines: ", count_lines)
logging.info("total line ")

total_character = len(content)
logging.info("total character ")

print("total character: ", total_character)

total_word = len(content.split())
logging.info("total word ")

print("total word: ", total_word)

