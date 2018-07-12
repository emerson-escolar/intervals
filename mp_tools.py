import intervals
import numpy

def get_data_in_paper():
    data = \
    {"fff" :
     ("4:4","3:4","3:3","2:4","2:3","1:4","2:2","1:3","1:2","1:1"),
     "ffb" :
     ("3:3","3:4","2:3","2:4","1:3","2:2","1:4","4:4","1:2","1:1"),
     "bfb" :
     ("3:3","1:1","3:4","1:3","2:3","1:4","2:4","1:2","4:4","2:2"),
     "bbf" :
     ("1:1","4:4","1:2","2:2","1:4","2:4","1:3","3:4","2:3","3:3"),
     "bbb" :
     ("1:1","1:2","2:2","1:3","2:3","1:4","3:3","2:4","3:4","4:4"),
     "fbb" :
     ("2:2","2:3","1:2","2:4","1:3","3:3","1:4","3:4","1:1","4:4"),
     "fbf" :
     ("4:4","2:2","2:4","1:2","2:3","1:4","3:4","1:3","3:3","1:1"),
     "bff" :
     ("4:4","3:4","1:1","3:3","1:4","2:4","1:3","2:3","1:2","2:2")}
    return data


def get_order_in_paper(orientation):
    data = get_data_in_paper()
    return data[orientation]


def interval_string_to_pair(code):
    assert len(code) == 3
    assert code[1] == ":"
    return (int(code[0])-1, int(code[2])-1)


def generate_mp_matrix(orientation):
    order = get_order_in_paper(orientation)
    ordered_pairs = [ interval_string_to_pair(x) for x in order ]

    n = len(ordered_pairs)
    ans = numpy.empty((n,n), dtype='object')

    for col in range(n):
        domain = ordered_pairs[col]
        for row in range(n):
            codomain = ordered_pairs[-row-1]


            if intervals.has_nonzero_zigzag_morphism(domain, codomain, orientation):
                ans[row,col] = "*"
            else:
                ans[row,col] = "_"
    return ans
