"""write file"""
import pickle

def write_file(path, data):
    """
    write file using pickle
    """
    pickle.dump(data, open(path, 'wb'))
