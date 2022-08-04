import nltk
import sys

from nltk.tree import Tree

TERMINALS = """
A -> "small" | "white"
N -> "cats" | "trees" 
V -> "climb" | "run"
"""

NONTERMINALS = """
S -> NP V
NP -> N | A NP 
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Comentado hasta terminar la primera parte del ejercicio
    # # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            #print(np)
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    lista = []
    for palabra in nltk.word_tokenize(sentence):
        if palabra.isalpha():
            lista.append(palabra.lower())
    return lista
    # raise NotImplementedError


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    lista =[]     
    for s in tree.subtrees():    
        if (s.label() == "NP") and len(s) == 1:    
            # print(f"s: {s}  len:= {len(s)}      label:= {s.label()}     height:= {s.height()}")
            lista.append(s)
    return lista
    # raise NotImplementedError


if __name__ == "__main__":
    main()
