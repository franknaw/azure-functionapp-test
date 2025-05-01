import azure.functions as func
import json
import logging

app = func.FunctionApp()


@app.function_name("api_hello_world")
@app.route(route="hello", methods=["POST,GET"], auth_level=func.AuthLevel.ANONYMOUS)
def api_hello_world(req: func.HttpRequest) -> func.HttpResponse:
    """
    Simple Hello World endpoint.
    """
    logging.info("Hello World endpoint called.")
    return func.HttpResponse(
        json.dumps({"message": "Hello, World!"}),
        status_code=200,
        mimetype="application/json"
    )
