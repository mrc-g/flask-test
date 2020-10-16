from flakon import JsonBlueprint
from flask import request, jsonify
from myservice.calculator import calculator as c


calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def sum():
    try:
        m = int(request.args.get('m'))
        n = int(request.args.get('n'))
    except ValueError:
        return jsonify({"result": "ValueError"})
    except TypeError:
        return jsonify({"result": "MissingArgument"})

    result = c.sum(m, n)

    return jsonify({'result': str(result)})


@calc.route('/calc/mul', methods=['GET'])
def mul():
    try:
        m = int(request.args.get('m'))
        n = int(request.args.get('n'))
    except ValueError:
        return jsonify({"result": "ValueError"})
    except TypeError:
        return jsonify({"result": "MissingArgument"})

    result = c.multiply(m, n)

    return jsonify({'result': str(result)})


@calc.route('/calc/div', methods=['GET'])
def div():
    try:
        m = int(request.args.get('m'))
        n = int(request.args.get('n'))
    except ValueError:
        return jsonify({"result": "ValueError"})
    except TypeError:
        return jsonify({"result": "MissingArgument"})

    try:
        result = c.divide(m, n)
    except ZeroDivisionError:
        return jsonify({"result": "DivisionByZeroError"})

    return jsonify({'result': str(result)})


@calc.route('/calc/sub', methods=['GET'])
def sub():
    try:
        m = int(request.args.get('m'))
        n = int(request.args.get('n'))
    except ValueError:
        return jsonify({"result": "ValueError"})
    except TypeError:
        return jsonify({"result": "MissingArgument"})

    result = c.subtract(m, n)

    return jsonify({'result': str(result)})
