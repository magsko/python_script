import json
from models import Item, Category, Shop

def create_shop(file_path: str) -> Shop:
    with open(file_path, "r", encoding="utf-8") as f:
        andriis_store = json.load(f)

    categories = []
    for category_data in andriis_store["categories"]:
        ukuleles = []
        for ukulele_data in category_data["items"]:
            ukulele = Item(
                name=ukulele_data["name"],
                price=ukulele_data["price"],
                quantity_in_stock=ukulele_data["quantityInStock"],
                color=ukulele_data["color"],
                in_stock=ukulele_data["inStock"],
            )
            ukuleles.append(ukulele)

        category = Category(
            category_name=category_data["categoryName"],
            items=ukuleles,
        )
        categories.append(category)

    return Shop(
        shop_name=andriis_store["shopName"],
        categories=categories,
    )


def add_category(shop: Shop, category_name: str):
    new_category = Category(
        category_name=category_name,
        items=[],
    )
    shop.categories.append(new_category)


def add_item(shop: Shop, category_name: str, name: str, price: int, quantity_in_stock: int, color: str,
             in_stock: bool):
    for category in shop.categories:
        if category.category_name == category_name:
            new_item = Item(
                name=name,
                price=price,
                quantity_in_stock=quantity_in_stock,
                color=color,
                in_stock=in_stock,
            )
            category.items.append(new_item)
            return



    print(f"Category '{category_name}' not found in Andrii's shop")

def save_shop(shop: Shop, file_path: str):
    categories = []
    for category in shop.categories:
        items = []
        for item in category.items:
            items.append({
                "name": item.name,
                "price": item.price,
                "quantityInStock": item.quantity_in_stock,
                "color": item.color,
                "inStock": item.in_stock,
            })

        categories.append({
            "categoryName": category.category_name,
            "items": items,
        })

    data = {
        "shopName": shop.shop_name,
        "categories": categories,
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def main():
    shop = create_shop("data/ukuleles.json")

    add_category(shop, "Baritone Ukuleles")
    add_item(
        shop,
        "Baritone Ukuleles",
        name="Baritone Ukulele",
        price=250,
        quantity_in_stock=15,
        color="Mahogany",
        in_stock=True,
    )
    save_shop(shop, "data/ukuleles_updated.json")

if __name__ == "__main__":
    main()
