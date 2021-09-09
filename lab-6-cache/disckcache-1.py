import diskcache as dc

cache = dc.Cache('tmp')
print(cache[b'key'])