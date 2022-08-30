import diffsync

data1 = {
    'a1': 'b1',
    'a2': 'b2'
}

data2 = {
    'a1': 'b3',
    'a2': 'b2'
}

diff_a_b = data1.diff_from(data2)