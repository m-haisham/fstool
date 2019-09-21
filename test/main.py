from fstool.external.regexfind import SubsetGraph, default_tests

if __name__ == '__main__':
    graph = SubsetGraph(default_tests)

    graph.add_regex('1234')
    graph.add_regex('12.4')
    graph.add_regex('1.+')

    print(graph.match('1234')[0].string)