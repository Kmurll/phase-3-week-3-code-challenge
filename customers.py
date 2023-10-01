from models import session, Review

class CustomerMethods:
    def __init__(self, customer):
        self.customer = customer

    # represent the class instances
    def __repr__(self):
        return f'{self.customer.id}: {self.customer.last_name}, {self.customer.first_name}\n'

    @property
    def customer_reviews(self):
        # Return a collection of all the reviews that the Customer has left
        customer = self.customer
        reviews = self.customer.reviews
        formatted_reviews = []

        for review in reviews:
            restaurant_name = review.restaurant.name
            star_rating = review.star_rating
            review_info = f"Review for {restaurant_name}: {star_rating} stars."
            formatted_reviews.append(review_info)

        # Combine formatted reviews into a single string with line breaks
        formatted_reviews_string = '\n'.join(formatted_reviews)
        return formatted_reviews_string


    @property
    def customer_restaurants(self):
        # Return a collection of all the restaurants that the Customer has reviewed
        reviewed_restaurants = self.customer.restaurants
        if not reviewed_restaurants:
            return "No reviewed restaurant"
        formatted_restaurants = [
            f"{restaurant.name} - Price: ${restaurant.price:.2f}"
            for restaurant in reviewed_restaurants           
        ]
        formatted_restaurants_string = "\n".join(formatted_restaurants)
        return formatted_restaurants_string



    @property
    def full_name(self):
        # Return the full name of the customer, with the first name and last name concatenated
        return f"{self.customer.first_name} {self.customer.last_name}"

    @property
    def favorite_restaurant(self):
    # Check if the customer has left any reviews
        if self.customer.reviews:
        # Sort reviews by star rating in descending order
            reviews = sorted(self.customer.reviews, key=lambda r: r.star_rating, reverse=True)
            return reviews[0].restaurant  # Return the restaurant with the highest rating
        else:
            return None  # Return None if the customer has not left any reviews


    def add_review(self, restaurant, rating):
        # Create a new review for the restaurant with the given rating
        new_review = Review(
            restaurant_id=restaurant.id,
            customer_id=self.customer.id,
            star_rating=rating
        )
        session.add(new_review)
        session.commit()
        return new_review

    def delete_reviews(self, restaurant):
        # Remove all reviews by this customer for a specific restaurant
        reviews_to_delete = [review for review in self.customer.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()
        print(f'{self.customer.first_name}\'s reviews for \'{restaurant.name} restaurant\' have been successfully deleted!')
