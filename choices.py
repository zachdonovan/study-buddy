import random
_urls = [
  "http://google.com",
  "http://amazon.com",
  "http://twitter.com",
]

def start_ix():
  # choose a random starting point
  return random.randrange(len(_urls))

def next_url(ix):
  # rotate through the available options
  if ix >= len(_urls)-1:
    ix = 0
  else:
    ix += 1

  return _urls[ix], ix


