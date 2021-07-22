from h2o_wave import Q, main, app, ui

@app('/counter', mode='broadcast')
async def serve(q: Q):
    bean_count = q.app.bean_count or 0
    if q.args.increment:
        q.app.bean_count = bean_count = bean_count + 1

    if not q.client.initialized:
        q.client.initialized = True
        q.page['beans'] = ui.form_card(
            box='1 1 1 2',
            items=[
                ui.button(
                    name='increment',
                    label='Click me!',
                    caption=f'{bean_count} beans',
                    primary=True,
                ),
            ],
        )
    else:
        q.page['beans'].items[0].button.caption = f'{bean_count} beans'
    await q.page.save()