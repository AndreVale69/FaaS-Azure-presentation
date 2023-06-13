import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    sum = req_body["val1"] + req_body["val2"]
    return func.HttpResponse(
            f"This HTTP triggered function executed successfully.\nIl risultato e': {sum}",
            status_code=200
    )
