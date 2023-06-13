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
                # create result string
                nums_prime = calc_prime(op1, op2)
                return func.HttpResponse(
                        f"This HTTP triggered function executed successfully.\nPrime numbers in the range [{op1} - {op2}]: [\n{nums_prime}\n]",
                        status_code=200
                )
        except:
                # if don't exist -> error page
                return func.HttpResponse(
                        f"Error! Use params: ?op1=value&op2=value",
                        status_code=200
                )

def calc_prime(val1: int, val2: int) -> str:
        res: str = ""
        # check prime numbers
        for value in range(val1, val2+1):
                if value > 1:
                        is_prime = True
                        for i in range(2, value):
                                if (value % i) == 0:
                                        is_prime = False
                                        break
                        if is_prime:
                                res = res + str(value) + ",\n"
        return res[:-2]
