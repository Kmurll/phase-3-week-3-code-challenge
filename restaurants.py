from models import session, Restaurant

class RestaurantMethods:
    def __init__(self, restaurant):
        self.restaurant = restaurant

        # represent the class instances
    def __repr__(self):
        return f'{self.restaurant.name} Restaurant - Price: ksh{self.restaurant.price}\n'

    def restaurant_reviews(self):
        # Return a collection of all the reviews for this restaurant
        reviews = self.restaurant.reviews
        formatted_reviews = []
            
        for review in reviews:
            customer_name = f"{review.customer.first_name} {review.customer.last_name}"
            review_info = f"Review by {customer_name}: {review.star_rating} stars."
            formatted_reviews.append(review_info)

        # Combine formatted reviews into a single string with line breaks
        formatted_reviews_string = '\n'.join(formatted_reviews)
        return formatted_reviews_string


    def restaurant_customers(self):
        # Return a collection of all the customers who reviewed the restaurant
        customers = self.restaurant.customers
        formatted_customers = []

        for customer in customers:
            customer_info = f"{customer.id}: {customer.first_name}, {customer.last_name}"
            formatted_customers.append(customer_info)

        # Combine formatted customer info into a single string with line breaks
        formatted_customers_string = '\n' + '\n'.join(formatted_customers)
        return formatted_customers_string


    @classmethod
    def fanciest_restaurant(cls):
        # Return the restaurant instance with the highest price
        return session.query(Restaurant).order_by(Restaurant.price.desc()).first()

    def all_reviews(self):
        # Return a list of strings with all the reviews for this restaurant
        reviews = []
        for review in self.restaurant.reviews:
            restaurant_name = review.restaurant.name
            customer_name = f"{review.customer.first_name} {review.customer.last_name}"
            review_info = f"Review for {restaurant_name} Restaurant by {customer_name}: {review.star_rating} stars."
            reviews.append(review_info)
        reviews_with_line_breaks = '\n'.join(reviews)
        return reviews_with_line_breaks
