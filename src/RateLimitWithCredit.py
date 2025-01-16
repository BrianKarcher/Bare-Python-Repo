import time
from threading import Lock

class RateLimiter:
    def __init__(self, credits_per_interval, interval_seconds):
        """
        Initialize the rate limiter.

        :param credits_per_interval: Amount of credit added per interval.
        :param interval_seconds: Duration of each interval in seconds.
        """
        self.credits_per_interval = credits_per_interval
        self.interval_seconds = interval_seconds
        self.customer_data = {}  # Stores customer credit and last update time.
        self.lock = Lock()

    def _add_credits(self, customer_id):
        """
        Add credits to a customer's account based on elapsed time.

        :param customer_id: ID of the customer.
        """
        current_time = time.time()

        if customer_id not in self.customer_data:
            # Initialize customer data if it doesn't exist.
            self.customer_data[customer_id] = {
                "credits": 0,
                "last_updated": current_time
            }

        customer = self.customer_data[customer_id]
        elapsed_time = current_time - customer["last_updated"]

        if elapsed_time >= self.interval_seconds:
            # Calculate how many intervals have passed.
            intervals = int(elapsed_time / self.interval_seconds)
            additional_credits = intervals * self.credits_per_interval

            # Update customer's credits and last update time.
            customer["credits"] += additional_credits
            customer["last_updated"] = current_time

    def consume(self, customer_id, credits):
        """
        Attempt to consume credits for a customer.

        :param customer_id: ID of the customer.
        :param credits: Amount of credits to consume.
        :return: True if the credits were successfully consumed, False otherwise.
        """
        with self.lock:
            self._add_credits(customer_id)
            
            if self.customer_data[customer_id]["credits"] >= credits:
                self.customer_data[customer_id]["credits"] -= credits
                return True
            else:
                return False

# Example usage
if __name__ == "__main__":
    # Create a rate limiter that adds 10 credits every 5 seconds.
    rate_limiter = RateLimiter(credits_per_interval=10, interval_seconds=5)

    customer_id = "customer1"

    # Simulate credit consumption.
    print(rate_limiter.consume(customer_id, 5))  # True: 5 credits consumed, 5 remaining.
    time.sleep(6)  # Wait for 6 seconds to accumulate credits.
    print(rate_limiter.consume(customer_id, 15))  # False: Not enough credits.
    print(rate_limiter.consume(customer_id, 10))  # True: Enough credits after the interval.