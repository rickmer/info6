from info6 import address
def add_missing_blocks_test1():
    assert address.add_missing_blocks('::0001') == '0000:0000:0000:0000:0000:0000:0000:0001'
