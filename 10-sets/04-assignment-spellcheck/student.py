def spellcheck(document, valid_words):
    final_result = set()
    valid_set = set(valid_words)
    valid_document = set(document)

    for x in valid_document:
        if x not in valid_set:
            final_result.add(x)
    
    return final_result