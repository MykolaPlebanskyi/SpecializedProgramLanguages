import variables


def store_result(identifier, result):
    variables.memory[identifier] = result


def retrieve_result(identifier):
    return variables.memory.get(identifier, None)


def working_memory(result):
    memory_text = input(variables.memory_text)
    if memory_text.lower() == "yes":
        save = input(variables.save)
        if save.lower() == "yes":
            identifier_save = input(variables.identifier_save)
            store_result(identifier_save, result)
        retrieve = input(variables.retrieve)
        if retrieve.lower() == "yes":
            identifier_retrieve = input(variables.identifier_retrieve)
            saved_result = retrieve_result(identifier_retrieve)
            if saved_result is not None:
                print(f"Result from memory: {saved_result:.2f}")
            else:
                print(f"Saved result with ID '{identifier_retrieve}' not found.")
