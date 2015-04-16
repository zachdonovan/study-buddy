import random
_urls = [
'https://docs.google.com/a/columbia.edu/forms/d/18__hOdGvK-FFqHYmbgACWUTuSGtUHZrbGe2LXh5VRpA/viewform',
'https://docs.google.com/a/columbia.edu/forms/d/1nsjxooZk1RmeGD22VJs1lt7D2476r83xJaskZUnNnkQ/viewform'
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


