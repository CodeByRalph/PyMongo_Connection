from configuration import app, client, printer, HTTPException
from database.schemas import all_data
from database.models import Sale

# Inserts Object into Transaction Collection
@app.post("/create_sale/")
def create_sale(new_sale: Sale):
    Transactions_Collection = client.Sales.Transactions
    try:
        Transactions_Collection.insert_one(dict(new_sale))
        return {"status_code":200, "id":str(Transactions_Collection.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

#Finds all Sales in the Transactions Collection in the Sales DB
@app.get("/sales")
def find_all_Sales():
    db = client.Sales.Transactions.find()
    return all_data(db)
