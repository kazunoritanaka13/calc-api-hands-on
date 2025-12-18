import json
import os
import sys

# Ensure project root is in sys.path so we can import calc_service
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from calc_service import multiply as multiply_impl

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        a = int(req.params.get('A'))
        b = int(req.params.get('B'))
    except Exception:
        # Per spec, we don't handle invalid inputs specially; return 400
        return func.HttpResponse(json.dumps({"error": "invalid input"}), status_code=400, mimetype="application/json")

    result = multiply_impl(a, b)
    return func.HttpResponse(json.dumps({"result": result}), status_code=200, mimetype="application/json")
