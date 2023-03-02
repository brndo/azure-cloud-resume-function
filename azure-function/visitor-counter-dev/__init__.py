import logging
import azure.functions as func


def main(req: func.HttpRequest, doc:func.DocumentList, outputDocument:func.Out[func.DocumentList]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #retrieve counter from comosdb
    old_counter_value = ""
    for d in doc:
        old_counter_value = {
           "count": d['count']
        }    

    #add one to counter
    temp_counter = str(old_counter_value['count'])
    temp_counter = int(temp_counter)
    new_counter_value = temp_counter + 1
    
    #update comos db

    outputDocument.set(func.Document.from_dict({"id": '11fb8b01-3244-473d-9c4e-02b16efa47b6', "count": new_counter_value}))
    
    logging.info('New counter value = ' + str(new_counter_value) + 'and old counter value = ' + str(old_counter_value))

    # send new counter value as return to http response
    return func.HttpResponse(
            str(new_counter_value),
            status_code=200,
            mimetype="text/plain"            
    )