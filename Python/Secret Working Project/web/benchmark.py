import timeit
from web_browse import WebBrowse as wb

if __name__ == '__main__':
    start = timeit.timeit()
    test = WebBrowse()
    test.search_by_file("craft-popular-urls",async_search = False)
    end = timeit.timeit()
    print("Took time {t}".format(t = str(end-start)))
