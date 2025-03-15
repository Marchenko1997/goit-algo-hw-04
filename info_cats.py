def get_cats_info(path: str) -> list[dict]:
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        cat_dict = {
                            "id": parts[0],
                            "name": parts[1],
                            "age": int(parts[2])
                        }
                        cats_list.append(cat_dict)

        return cats_list
    
    except FileNotFoundError:
        print("File not found. Check the path.")
        return []
    
    except ValueError:
        print("Invalid data in the file. Check the format.")
        return []

file_path = "cats.txt"

cats_info = get_cats_info(file_path)

for cat in cats_info:
    print(cat)
