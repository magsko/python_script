from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: int
    quantity_in_stock: int
    color: str
    in_stock: bool


@dataclass
class Category:
    category_name: str
    items: list[Item]


@dataclass
class Shop:
    shop_name: str
    categories: list[Category]