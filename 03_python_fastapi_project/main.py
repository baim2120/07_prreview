from contextlib import asynccontextmanager
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from database import Product, CartItem, create_tables, get_db

app = FastAPI(title=settings.app_name)


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    name: str
    price: float


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str | None = None
    stock: int


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    description: str | None = None
    stock: int | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None
    stock: int


def product_to_response(product: Product):
    return ProductResponse(id=product.id, name=product.name, price=product.price, description=product.description, stock=product.stock)


def products_to_response(products: List[Product]):
    return [product_to_response(product) for product in products]


def cartitem_to_response(cartitem: CartItem):
    return CartItemResponse(
        id=cartitem.id,
        product_id=cartitem.product_id,
        quantity=cartitem.quantity,
        name=cartitem.product.name if cartitem.product else "",
        price=cartitem.product.price if cartitem.product else 0.0
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    db_product: Product = (await db.execute(select(Product).filter(Product.name == product.name))).first()

    if db_product:
        raise HTTPException(
            status_code=400, detail=f"Product with name `{product.name}` already registered")

    db_product = Product(name=product.name,
                         price=product.price,
                         description=product.description,
                         stock=product.stock)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return product_to_response(db_product)


@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate, db: AsyncSession = Depends(get_db)):
    db_product: Product = (await db.execute(select(Product).filter(Product.id == product_id))).scalars().first()

    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id `{product_id}` not found")

    db_product_with_name: Product = (await db.execute(select(Product).filter((Product.name == product.name) & (Product.id != product_id)))).first()

    if db_product_with_name:
        raise HTTPException(
            status_code=400, detail=f"Another product with name `{product.name}` already registered")

    if product.name is not None:
        db_product.name = product.name

    if product.price is not None:
        db_product.price = product.price

    if product.description is not None:
        db_product.description = product.description

    if product.stock is not None:
        db_product.stock = product.stock

    await db.commit()
    await db.refresh(db_product)

    return product_to_response(db_product)


@app.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product: Product = (await db.execute(select(Product).filter(Product.id == product_id))).scalars().first()

    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id `{product_id}` not found")

    await db.delete(db_product)
    await db.commit()

    return product_id


@app.get("/products/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    products = (await db.execute(select(Product))).scalars().all()
    return products_to_response(products)


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product: Product = (await db.execute(select(Product).filter(Product.id == product_id))).scalars().first()

    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id `{product_id}` not found")

    return product_to_response(db_product)


@app.post("/cart/add/{product_id}", response_model=CartItemResponse)
async def add_to_cart(product_id: int, db: AsyncSession = Depends(get_db)):
    # Get product
    db_product: Product = (await db.execute(select(Product).filter(Product.id == product_id))).scalars().first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    if db_product.stock < 1:
        raise HTTPException(status_code=400, detail="Out of stock")
    # Check if already in cart
    db_cartitem: CartItem = (await db.execute(select(CartItem).filter(CartItem.product_id == product_id))).scalars().first()
    if db_cartitem:
        db_cartitem.quantity += 1
    else:
        db_cartitem = CartItem(product_id=product_id, quantity=1)
        db.add(db_cartitem)
    # Decrement stock
    db_product.stock -= 1
    await db.commit()
    await db.refresh(db_cartitem)
    return cartitem_to_response(db_cartitem)


@app.post("/cart/remove/{cart_item_id}", response_model=CartItemResponse)
async def remove_from_cart(cart_item_id: int, db: AsyncSession = Depends(get_db)):
    db_cartitem: CartItem = (await db.execute(select(CartItem).filter(CartItem.id == cart_item_id))).scalars().first()
    if not db_cartitem:
        raise HTTPException(status_code=404, detail="Item not in cart")
    db_product: Product = (await db.execute(select(Product).filter(Product.id == db_cartitem.product_id))).scalars().first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Store the response before we potentially delete the cart item
    response = cartitem_to_response(db_cartitem)
    
    db_cartitem.quantity -= 1
    db_product.stock += 1
    
    if db_cartitem.quantity <= 0:
        await db.delete(db_cartitem)
    
    await db.commit()
    
    # Return the stored response
    return response


@app.get("/cart/", response_model=List[CartItemResponse])
async def get_cart(db: AsyncSession = Depends(get_db)):
    cart_items = (await db.execute(select(CartItem))).scalars().all()
    # Eager load product for each cart item
    for item in cart_items:
        _ = item.product
    return [cartitem_to_response(item) for item in cart_items]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
