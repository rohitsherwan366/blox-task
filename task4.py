import time

class APICaller:
    def __init__(self, limit, penalty):
        self.limit = limit
        self.penalty = penalty
        self.bucket = limit
        self.last_refill_time = time.time()

    def call_me(self, input):
        current_time = time.time()

        # Refill the bucket based on elapsed time and limit
        elapsed_time = current_time - self.last_refill_time
        refill_amount = elapsed_time * (self.limit / 60)
        self.bucket = min(self.bucket + refill_amount, self.limit)  # Ensure bucket doesn't exceed the limit
        self.last_refill_time = current_time

        # Check if there are enough tokens in the bucket to make the call
        if self.bucket >= 1:
            self.bucket -= 1
            print(f"Making API call with input: {input}")
        else:
            # Penalty - Wait until the bucket is refilled
            wait_time = (1 - self.bucket) * (60 / self.limit) + self.penalty
            print(f"Exceeded API limit. Waiting for {wait_time:.2f} seconds...")
            time.sleep(wait_time)
            self.call_me(input)  # Recursive call after the penalty

# Example usage
api = APICaller(limit=15, penalty=60)

# Make 20 API calls per minute
for i in range(20):
    api.call_me(f"Input {i+1}")

# Additional API calls after the penalty period
api.call_me("Additional call 1")
api.call_me("Additional call 2")
