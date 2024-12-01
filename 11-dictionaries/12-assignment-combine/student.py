def combine(d1, d2):
    combined_dict = {}
    for english, dutch in d1.items():
        if dutch in d2:  # Check if there is a French translation for this Dutch word
            combined_dict[english] = d2[dutch]  # Add English to French translation
    return combined_dict
