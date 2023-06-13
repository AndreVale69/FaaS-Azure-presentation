import logging

import azure.functions as func

# calcola-somma function
def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')

        # with req.method you can obtain REST method (GET, POST, etc.)
        # but doesn't matter (watch function.json)
        
        try:
                # try to obtain op1 & op2 operators 
                op1 = int(req.params.get("op1"))
                op2 = int(req.params.get("op2"))
                sum = op1 + op2
                return func.HttpResponse(
                        f"This HTTP triggered function executed successfully.\nThe result is: {op1} + {op2} = {sum}",
                        status_code=200
                )
        except:
                # if don't exist -> error page
                return func.HttpResponse(
                        f"Error! Use params: ?op1=value&op2=value",
                        status_code=200
                )
