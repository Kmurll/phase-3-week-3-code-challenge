#!/usr/bin/env python3

from models import *
from restaurants import RestaurantMethods
from customers import CustomerMethods
from reviews import ReviewMethods

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # import ipdb; ipdb.set_trace()

    '''----------------------------------- RESTAURANT -------------------------------------------'''
    restaurant1 = session.query(Restaurant).first()

    # Create an instance of RestaurantMethods
    restaurant_methods = RestaurantMethods(restaurant1)

    # return details of all the restaurant instance reviews
    print('\n-------------------------ALL REVIEWS-------------------------')
    print(restaurant_methods.all_reviews())

    print()
    print('\n------------------------- RESTAURANT SECTION ------------------------')
    print('------------------------- Restaurant One -----------------------------')
    print(restaurant_methods)

    # return all the restaurant instance reviews
    print("\n-------------------- Restaurant's Review --------------------")
    print(restaurant_methods.restaurant_reviews())

    # return all the customers who have reviewed this restaurant
    print("\n-------------------- Restaurant's Customers --------------------")
    print(restaurant_methods.restaurant_customers())

    print('\n------------------------- Fanciest Restaurant -------------------------')
    # returns the fanciest(most-expensive) restaurant of all the restaurants
    print(restaurant_methods.fanciest_restaurant())



    
    '''------------------------------------ CUSTOMER ---------------------------------------------'''
    customer1 = session.query(Customer).first()
    customer_methods = CustomerMethods(customer1)
    
    print()
    print('\n------------------------- CUSTOMER SECTION ------------------------')
    print('------------------------ Customer One ---------------------------')
    print(customer_methods)

    print("\n------------------------ Customer's Reviews ------------------------")
    # returns the customer reviews
    print(customer_methods.customer_reviews)

    print("\n-------------------- Customer's Reviewed Restaurants --------------------")
    # returns the customer reviews
    print(customer_methods.customer_restaurants)

    print("\n-------------------------- Customer's Full Name -------------------------")
    # return customer full_name
    print(customer_methods.full_name)

    print('\n------------------------- Favorite Restaurant -------------------------')
    # return restaurant with the highest review for this customer
    print(customer_methods.favorite_restaurant)

    print('\n------------------------------ Add Review -----------------------------')
    # add review and return it
    print(customer_methods.add_review(restaurant1, 8))

    '''----------------------------------- REVIEWS ------------------------------------------------'''
    review1 = session.query(Review).first()
    review_methods = ReviewMethods(review1)

    print()
    print('\n------------------------ Review SECTION ------------------------')
    print('------------------------ Review One ----------------------------')
    print(review_methods)

    print("\n-------------------- Review's Owner(customer) --------------------")
    # return customer
    print(review_methods.review_customer())

    print("\n-------------------- Review's Target(restaurant) --------------------")
    # return restaurant
    print(review_methods.review_restaurant())

    print('\n--------------------------- Full Review ---------------------------')
    # return full review details
    print(review_methods.full_review())