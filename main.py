import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


app.add_url_rule('/', 'index', index)


@app.route('/matplotlib')
def matplotlib():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


app.add_url_rule('/matplotlib', 'matplotlib', matplotlib)
