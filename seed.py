from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Restaurant, Review, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Customer).delete()
    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.commit()


    fake = Faker()

    # ------------------------ Populate customer table --------------------------
    customers = []
    for i in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)


    # ----------------------- Populate restaurants table -----------------------
    restaurants = []
    for i in range(10):
        restaurant = Restaurant(
            name=fake.city(),
            price=random.randint(4000,10000)
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)

    # ------------------------ Populate reviews table ----------------------------
    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1,10)):
            customer = random.choice(customers)
            review = Review(
                restaurant_id=restaurant.id,
                star_rating=random.randint(1, 10),
                customer_id=customer.id
            )
            customer.reviews.append(review) #Associate the customer with the appended review
            session.add(review)

    session.commit()
    session.close()