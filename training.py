import pickle


def save(path: str, obj):
    with open(path, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load(path: str):
    with open(path, 'rb') as input:
        return pickle.load(input)
