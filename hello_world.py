import time
from h2o_wave import site, ui

page = site['/beer']

beer_card = page.add('wall', ui.markdown_card(
    box='1 1 4 2',
    title='99 Bottles of Beer',
    content='',
))

for i in range(99, 0, -1):
    beer_card.content = f"""
{i} bottles of beer on the wall, {i} bottles of beer.

Take one down, pass it around, {i - 1} bottles of beer on the wall...
"""
    page.save()
    time.sleep(1)