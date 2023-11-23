import difflib

text = "Oba tyto přístupy vytvoří nový text, ve kterém jsou znaky 'i' a 'y' vynechány. První příklad používá cyklus, který projde každý znak ve vstupním textu a přidá ho do výsledného textu pouze v případě, že znak není 'i' nebo 'y'. Druhý příklad využívá"
result = text.replace('i', '_').replace('y', '_')



def compare_strings(string1, string2):
    # Vytvoříme objekt difflib.Differ
    differ = difflib.Differ()

    # Porovnáme dva řetězce
    diff = list(differ.compare(string1, string2))

    # Zobrazíme rozdíly
    print('\n'.join(diff))

# Příklad použití

compare_strings(text, result)

print(result)