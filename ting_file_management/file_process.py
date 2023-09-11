from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    if file is not None:
        informations = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        if informations not in instance:
            instance.enqueue(informations)
            print(informations)


def remove(instance):
    if instance.is_empty():
        sys.stdout.write("Não há elementos\n")
    else:
        sys.stdout.write(
            f"Arquivo {instance.dequeue()['nome_do_arquivo']} "
            "removido com sucesso\n"
        )


def file_metadata(instance, position):
    if position not in range(len(instance._data)):
        sys.stderr.write("Posição inválida\n")
        return None

    metadata = instance.search(position)
    if metadata is not None:
        print(metadata)
