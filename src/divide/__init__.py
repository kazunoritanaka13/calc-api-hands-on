import json
import os
import sys

# Ensure project root is in sys.path so we can import calc_service
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from calc_service import divide as divide_impl

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        a = int(req.params.get('A'))
        b = int(req.params.get('B'))
    except Exception:
        return func.HttpResponse(json.dumps({"error": "invalid input"}), status_code=400, mimetype="application/json")

    # Per spec, B == 0 should not happen; but guard to avoid crash
    if b == 0:
        return func.HttpResponse(json.dumps({"error": "division by zero"}), status_code=400, mimetype="application/json")

    result = divide_impl(a, b)

    # If result is an integer value, return as int to match examples
    if float(result).is_integer():
        result = int(result)

    return func.HttpResponse(json.dumps({"result": result}), status_code=200, mimetype="application/json")
