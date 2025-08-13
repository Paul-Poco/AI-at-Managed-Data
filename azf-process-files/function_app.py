import azure.functions as func
from azure.storage.blob import BlobServiceClient
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="http_trigger")
@app.route(route="http_trigger", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.function_name(name="get_file")
@app.blob_trigger(arg_name="stinternalrag001", path="content", connection="AzureWebJobsStorage")
def get_file(my_blob: func.InputStream) -> func.HttpResponse:
    logging.info("Blob trigger function processed a blob.")

    file_name = my_blob.name

    return func.HttpResponse(f"Hello, {file_name}. This Blob triggered function executed successfully.")
