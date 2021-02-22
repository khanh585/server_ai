from flask import render_template, request, redirect, Blueprint
from flask import jsonify
import pyodbc
import torch
from IPython.display import Image, clear_output


todo = Blueprint('todo', __name__, url_prefix='/')

@todo.route('/', methods=['POST','GET'])
def index():
    return jsonify({"khanh":"ahihi"})


@todo.route('/checkGPU', methods=['GET'])
def checkGPU():
    torch_ver ='%s' % (torch.__version__)
    gpu ='%s' % (torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU')
    return jsonify({"torch_ver": torch_ver, "gpu":gpu})


