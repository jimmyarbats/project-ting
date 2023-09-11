import sys

def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")
            return None
        with open(path_file, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError as e:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None
