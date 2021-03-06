#! /usr/bin/env python


from brubeck.request_handling import Brubeck, http_response
from brubeck.templating import  load_jinja2_env
from brubeck.templating import Jinja2Rendering


app = Brubeck(mongrel2_pair=('ipc://127.0.0.1:9999',
                             'ipc://127.0.0.1:9998'),
              template_loader=load_jinja2_env('./templates/jinja2'))


@app.add_route('^/', method=['GET', 'POST'])
def index(application, message):
    name = message.get_argument('name', 'dude')
    context = {
        'name': name,
    }
    body = application.render_template('success.html', **context)
    return http_response(body, 200, 'OK', {})


app.run()
