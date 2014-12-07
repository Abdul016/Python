import data_load
import indexer
import WebParser
import WebSearcher
import FileSearcher


def webAndFile():
    data_load.get_traversal_data()
    file_data = indexer.read_data()
    web_data = WebParser.webData()
    print("File data search:")
    print("====================================================")
    FileSearcher.fileSearch(file_data)
    print("Web data search:")
    print("====================================================")
    WebSearcher.webSearcher(web_data)


webAndFile()
