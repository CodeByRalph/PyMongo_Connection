def individual_data(Sale):
    return {
        "id": str(Sale["_id"]),
        "Customer_Name": Sale['Customer_Name'],
        "Customer_Address": Sale['Customer_Address'],
        "Customer_Phone": Sale['Customer_Phone'],
        "Customer_Email": Sale['Customer_Email'],
        "Sale_Amount": Sale['Sale_Amount']
    }

def all_data(Sales):
    return [individual_data(Sale) for Sale in Sales]