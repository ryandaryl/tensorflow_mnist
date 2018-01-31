import base64
import requests
from cStringIO import StringIO
from scripts.lesson7 import fit_line

def png_encode(fig):
    io = StringIO()
    fig.savefig(io, format='png')
    return base64.encodestring(io.getvalue())

def run_script(filename):
    output = fit_line()
    return [png_encode(output[0])] + output[1:]