from pydantic import BaseModel

class Sale(BaseModel):
    Customer_Name: str
    Customer_Address: str
    Customer_Phone: str
    Customer_Email: str
    Sale_Amount: float