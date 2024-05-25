import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Value must be a string")
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split the string on '.', '?' and '!' using regular expressions
        sentences = re.split(r'[.!?]', self._value)
        # Remove empty strings resulting from consecutive punctuation marks
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())  # Output: False
print(string.is_question())  # Output: True
print(string.is_exclamation())  # Output: False
print(string.count_sentences())  # Output: 3

