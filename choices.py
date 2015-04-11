import random
_urls = [
  "http://google.com",
  "http://amazon.com",
  "http://twitter.com",
]
_url_ix = 0

def start():
  # choose a random starting point
  _url_ix = random.randrange(len(_urls))

def next():
  # rotate through the available options
  if _url_ix >= len(_urls):
    _url_ix = 0
  else:
    _url_ix += 1

  return _urls[_url_ix]


