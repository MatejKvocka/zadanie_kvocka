from flask import Flask, jsonify, make_response
import os
import psutil

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.errorhandler(400)
def handle_400_error(_error='Misunderstood'):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': str(_error)}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error='Server error'):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': str(_error)}), 500)


@app.route('/cpu/used', methods=['GET'])
def cpu_used():
    return jsonify(
        text="Total CPUs utilized percentage:",
        value=str(psutil.cpu_percent()) + "%"

    )


@app.route('/', methods=['GET'])
def index():
    return jsonify([
        "/cpu/used", "/cpu/cores/physical", "/cpu/cores/total","/cpu/frequency/current", "/cpu/frequency/max",
        "/cpu/frequency/min", "/ram/used","/ram/available", "/disk"
    ])


@app.route('/cpu/cores/physical', methods=['GET'])
def cpu_physical():
    return jsonify(
        text="Physical cores:",
        value=str(psutil.cpu_count(logical=False))

    )


@app.route('/cpu/cores/total', methods=['GET'])
def cpu_total():
    return jsonify(
        text="Total cores:",
        value=str(psutil.cpu_count(logical=True))

    )


@app.route('/cpu/frequency/current', methods=['GET'])
def cpu_frequency():
    return jsonify(
        text="Current frequency",
        value=str(psutil.cpu_freq().current)

    )


@app.route('/cpu/frequency/max', methods=['GET'])
def cpu_max_frequency():
    return jsonify(
        text="Max frequency",
        value=str(psutil.cpu_freq().max)
    )


@app.route('/cpu/frequency/min', methods=['GET'])
def cpu_min_frequency():
    return jsonify(
        text="Min frequency",
        value=str(psutil.cpu_freq().min)

    )


@app.route('/ram/used', methods=['GET'])
def ram_used():
    return jsonify(
        text="Percentage of used RAM:",
        value=str(psutil.virtual_memory().percent) + "%"
    )


@app.route('/ram/available', methods=['GET'])
def memory():
    return jsonify(
        text="Percentage of available RAM:",
        value=str(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) + "%"
    )


@app.route('/disk', methods=['GET'])
def disk_usage():
    return str(psutil.disk_usage(os.sep).percent)


app.run(host='0.0.0.0', port=5000)
