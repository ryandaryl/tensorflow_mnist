import base64
import requests
from cStringIO import StringIO
from scripts.mnist_softmax import main

def png_encode(fig):
    io = StringIO()
    fig.savefig(io, format='png')
    return base64.encodestring(io.getvalue())

def run_script():
    main(0)