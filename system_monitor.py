import time
import psutil
from h2o_wave import site, ui, data

page = site['/monitor']

cpu_card = page.add('cpu_stats', ui.small_series_stat_card(
    box='1 1 1 1',
    title='CPU',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$red',
))
mem_card = page.add('mem_stats', ui.small_series_stat_card(
    box='1 2 1 1',
    title='Memory',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$blue',
))

tick = 0
while True:
    tick += 1

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_card.data.usage = cpu_usage
    cpu_card.plot_data[-1] = [tick, cpu_usage]

    mem_usage = psutil.virtual_memory().percent
    mem_card.data.usage = mem_usage
    mem_card.plot_data[-1] = [tick, mem_usage]

    page.save()
    time.sleep(1)