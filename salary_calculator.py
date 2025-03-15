def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [int(line.split(",")[1])for line in file if line.strip()]

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0

            return total, average

    except FileNotFoundError:
         print("File not found. Check the path.")
         return 0, 0
    
    except ValueError:
        print("Invalid data in the file. Check the format.")
        return 0, 0
    
    file_path = "salaries.txt"

    total, average = total_salary(file_path)

    print(f"Total salary amount: {total}, Average salary: {average:.2f}")