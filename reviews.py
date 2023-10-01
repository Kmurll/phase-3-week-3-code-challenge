from models import Review

class ReviewMethods:
    def __init__(self,review):
        self.review = review

    # represent the class instances
    def __repr__(self):
        return (f" {self.review}")

    def review_customer_name(self):
        return self.review.customer.full_name

    def review_rating(self):
        return self.review           

    def review_customer(self):
        # Return the Customer instance for this review
        customer_name = f"{self.review.customer.first_name} {self.review.customer.last_name}"
        return customer_name

    def review_restaurant(self):
        # Return the Restaurant instance for this review
        return self.review.restaurant

    def full_review(self):
        customer_name = f"{self.review.customer.first_name} {self.review.customer.last_name}"
        return f"Review for {self.review.restaurant} Restaurant by {customer_name}: {self.review.star_rating} stars"
