from pathlib import Path
import os
import sys

current_path = Path(os.path.abspath(__file__)).parent

#Get wanted number
if len(sys.argv) < 2:
    exit(-1)

wanted_number = int(sys.argv[1])

if wanted_number < 1:
    exit(-1)

number_100 = wanted_number // 100 * 100
if number_100 == wanted_number:
    range_100 = (number_100 - 99, number_100)
else:
    range_100 = (number_100 + 1, number_100 + 100)

number_10 = number_100 + (wanted_number % 100) // 10 * 10
if wanted_number % 10 == 0:
    range_10 = (number_10 - 9, number_10)
else:
    range_10 = (number_10 + 1, number_10 + 10)

folder_100 = "Problems_" + "_".join(map(str, range_100))
folder_10 = "Problems_" + "_".join(map(str, range_10))
folder_1 = "Problem_" + str(wanted_number)

final_path = current_path / folder_100 / folder_10 / folder_1
final_path.mkdir(parents=True, exist_ok=True)

(final_path / "problem.txt").touch()
(final_path / "solution.py").touch()