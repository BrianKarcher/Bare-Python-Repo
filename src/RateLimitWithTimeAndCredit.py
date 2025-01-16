import time
from threading import Lock
from collections import deque

class RateLimiter:
    def __init__(self, max_requests, time_window, max_credits):
        """
        Initialize the rate limiter.

        :param max_requests: Maximum number of requests allowed per time_window.
        :param time_window: Time window in seconds.
        :param max_credits: Maximum number of credits allowed.
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.max_credits = max_credits
        
        self.lock = Lock()
        self.credits = max_credits
        self.requests = deque()  # Store timestamps of requests

    def allow_request(self):
        """
        Determines if a request is allowed based on time and credit limits.

        :return: True if the request is allowed, False otherwise.
        """
        with self.lock:
            now = time.time()

            # Remove requests that are outside the current time window
            while self.requests and self.requests[0] <= now - self.time_window:
                self.requests.popleft()

            # Check time-based limit
            if len(self.requests) < self.max_requests:
                self.requests.append(now)
                return True

            # Check credit-based limit
            if self.credits > 0:
                self.credits -= 1
                return True

            return False

    def add_credits(self, credits):
        """
        Add credits to the rate limiter, respecting the max_credits limit.

        :param credits: Number of credits to add.
        """
        with self.lock:
            self.credits = min(self.max_credits, self.credits + credits)

    def get_status(self):
        """
        Returns the current status of the rate limiter.

        :return: A dictionary with current credits and number of requests in the time window.
        """
        with self.lock:
            return {
                "credits": self.credits,
                "requests_in_window": len(self.requests)
            }

# Example usage
if __name__ == "__main__":
    limiter = RateLimiter(max_requests=5, time_window=10, max_credits=3)

    for i in range(10):
        time.sleep(1)
        if limiter.allow_request():
            print(f"Request {i + 1} allowed.")
        else:
            print(f"Request {i + 1} denied.")

    # Add credits
    print("Adding 2 credits.")
    limiter.add_credits(2)
    print("Status:", limiter.get_status())