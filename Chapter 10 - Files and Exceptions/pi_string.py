from pathlib import Path

reader   = Path('D:/Recent Work/My Learning/Python/Python Crash Course - Book/pcc_3e-main/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt')
contents = reader.read_text().strip()
lines    = contents.splitlines()

for line in lines[:50]:
    print(line.strip())
