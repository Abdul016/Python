import pickle

def raw_data():
    data = pickle.load(open("raw_data.pickle","rb"))
    return data


