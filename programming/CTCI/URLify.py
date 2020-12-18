def urlify(word: str) -> str:
    return word.strip().replace(" ", "%20")

print(urlify("Mr Vamsi Krishna     "))