import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User, Profile, Post, Order, Product
from core.models import db_helper
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import selectinload, joinedload


async def create_user(username: str, session: AsyncSession) -> User:
    user: User = User(username=username)
    session.add(user)
    await session.commit()
    print("user", user)
    return user

async def get_user_by_username(username: str, session: AsyncSession):
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    print("user", username, user)
    return user


async def create_user_profile(
        user_id: int,
        session: AsyncSession,
      first_name: str | None = None,
      last_name: str | None = None
      ) -> Profile:
    profile = Profile(user_id=user_id, first_name=first_name, last_name=last_name)
    session.add(profile)
    await session.commit()
    return  profile



async def create_user_posts(user_id: int, session: AsyncSession, *titles: str) -> list[Post]:
    posts = [Post(user_id=user_id, title=title) for title in titles]
    session.add_all(posts)
    await session.commit()
    return posts



async def get_users_with_posts(session: AsyncSession) -> list[User]:
    stmt = select(User).options(selectinload(User.posts)).order_by(User.id)
    results: Result = await session.scalars(stmt)

    for user in results:
        print(user)
        for post in user.posts:
            print(post.title)

    return results

async def get_posts_with_users(session: AsyncSession) -> list[Post]:
    stmt = select(Post).options(joinedload(Post.users)).order_by(Post.id)
    results: Result = await session.scalars(stmt)
    return results


async def get_profiles_with_users_and_posts_filter(post_id: int, session: AsyncSession) -> list[Post]:
    stmt = select(Profile).options(joinedload(Profile.user).selectinload(User.posts)).order_by(Profile.id)


async def create_orders_with_products(session: AsyncSession):
    order_1 = await create_order(session=session)
    order_promo = await create_order(session=session, promocode="Alpha")

    laptop = await create_product(session=session, name="Laptop", price=300)
    iphone = await create_product(session=session, name="Iphone", price=300, description="XR")

    stmt = select(Order).options(selectinload(Order.products)).order_by(Order.id)

    order_one = await session.scalar(select(Order).options(selectinload(Order.products)).where(Order.id == order_1.id))
    order_two = await session.scalar(
        select(Order)
        .options(selectinload(Order.products))
        .where(Order.id == order_promo.id)
    )

    order_one.products.append(laptop)
    order_two.products.append(iphone)

    await session.commit()


async def get_orders_with_products(session: AsyncSession):
    stmt = select(Order).options(selectinload(Order.products)).order_by(Order.id)
    results = await session.scalars(stmt)

    return list(results)


async def demo_get_orders_and_products_wrom_secondary(session: AsyncSession):
    await create_orders_with_products(session=session)

    orders = await get_orders_with_products(session=session)

    for order in orders:
        print(order.promocode, order.creation_date)
        for product in order.products:
            print(product.name, product.price)







async def create_order(session: AsyncSession, promocode: str | None = None) -> Order:
    order = Order(promocode=promocode)
    session.add(order)
    await session.commit()
    return order


async def create_product(session: AsyncSession, name: str, price: int, description: str | None = None) -> Product:
    product = Product(name=name, description=description, price=price)
    session.add(product)
    await session.commit()
    return product

async def main():
    async with db_helper.session() as session:

        # created_user_second = await create_user(username="Alex", session=session)
        # alex_user = await create_user(username="Migielsaa", session=session)
        # alexey_user = await create_user(username="Alenaf", session=session)
        #
        # await create_user_profile(user_id=alex_user.id, session=session)
        # await create_user_profile(user_id=alexey_user.id, session=session)
        #
        # await create_user_posts(alexey_user.id, session, "SQL", "SQLAlchemy")
        # users = await get_users_with_posts(session=session)
        # print(users)
        await demo_get_orders_and_products_wrom_secondary(session=session)




if __name__ == "__main__":
    asyncio.run(main())



