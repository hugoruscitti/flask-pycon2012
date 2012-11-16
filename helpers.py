from flask import render_template

def helper_pie(values, title="untitled", size=100):
    id = 123
    size = int((400 / 100.0) * size)
    return render_template('pie.html', id=id, size=size, title=title, values=values)

def helper_chart(values, title="untitled", size=100):
    id = 123
    size = int((400 / 100.0) * size)
    return render_template('chart.html', id=id, size=size, title=title, values=values)

def load(app):
    @app.context_processor
    def helpers_personalizados():
        return {'pie': helper_pie, 'chart': helper_chart}
