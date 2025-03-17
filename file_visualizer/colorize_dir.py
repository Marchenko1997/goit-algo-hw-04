import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)

def print_dir_structure(directory: Path, prefix=""):
  
    if not directory.is_dir():
        print(Fore.RED + f"Error: {directory} is not a directory!")
        return

   
    entries = list(directory.iterdir())

    for index, entry in enumerate(entries):
        connector = "┗━━ " if index == len(entries) - 1 else "┣━━ "

      
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + f"📂 {entry.name}")
         
            print_dir_structure(entry, prefix + ("    " if index == len(entries) - 1 else "┃   "))
     
        else:
            print(prefix + connector + Fore.GREEN + f"📜 {entry.name}")

if __name__ == "__main__":
  
    if len(sys.argv) < 2:
        print(Fore.RED + "Ошибка: Укажите путь к директории!")
        sys.exit(1)

 
    dir_path = Path(sys.argv[1])

    
    if not dir_path.exists():
        print(Fore.RED + f"Ошибка: Путь '{dir_path}' не существует!")
        sys.exit(1)

  
    print_dir_structure(dir_path)
