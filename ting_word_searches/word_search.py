def exists_word(word, instance):
    result = []

    for file_index in range(len(instance)):
        file_data = instance.search(file_index)
        events = [
            {"linha": line_num}
            for line_num, line in enumerate(
                file_data["linhas_do_arquivo"], start=1
            )
            if word.lower() in line.lower()
        ]

        if events:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": events,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
