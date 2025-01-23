from typing import List, Dict
from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: Dict) -> 'Product':
        """
        Load a Product instance from a dictionary.
        """
        return Product(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            cost=data.get('cost'),
            qty=data.get('qty', 0)  # Default quantity to 0 if not provided
        )


def list_products() -> List[Product]:
    """
    Retrieve and return a list of all products.
    """
    products_data = dao.list_products()
    return [Product.load(product) for product in products_data]


def get_product(product_id: int) -> Product:
    """
    Retrieve and return a single product by its ID.
    """
    product_data = dao.get_product(product_id)
    return Product.load(product_data)


def add_product(product: Dict):
    """
    Add a new product to the database.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Update the quantity of a product. Raises an error if the quantity is negative.
    """
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)