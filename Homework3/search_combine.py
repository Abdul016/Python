import data_load
import searcher
import indexer


def mainSearch():
    data_load.get_traversal_data()
    data = indexer.raw_data()
    searcher.searchQuery(data)


mainSearch()
