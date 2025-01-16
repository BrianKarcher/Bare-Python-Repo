from collections import deque
from time import time

class RateLimiter:
    def __init__(self):
        # Dictionary to store keys and their timestamp queues
        self.key_access = {}

    def rate_limit(self, key: str, interval: int, max_limit: int) -> bool:
        """
        Check if a given key can be accessed within the specified rate limits.

        :param key: The key to check.
        :param interval: Time interval in seconds.
        :param max_limit: Maximum number of accesses allowed in the interval.
        :return: True if access is allowed, False otherwise.
        """
        current_time = time()

        # Initialize the deque for the key if it doesn't exist
        if key not in self.key_access:
            self.key_access[key] = deque()

        # Remove timestamps that are outside the interval window
        while self.key_access[key] and current_time - self.key_access[key][0] > interval:
            self.key_access[key].popleft()

        # Check if the current number of accesses is within the limit
        if len(self.key_access[key]) < max_limit:
            self.key_access[key].append(current_time)
            return True
        else:
            return False

# Example usage
if __name__ == "__main__":
    rate_limiter = RateLimiter()

    # Simulate calls to rate_limit
    key = "device_info"
    interval = 30
    max_limit = 3

    print(rate_limiter.rate_limit(key, interval, max_limit))  # True
    print(rate_limiter.rate_limit(key, interval, max_limit))  # True
    print(rate_limiter.rate_limit(key, interval, max_limit))  # True
    print(rate_limiter.rate_limit(key, interval, max_limit))  # False (if within interval)