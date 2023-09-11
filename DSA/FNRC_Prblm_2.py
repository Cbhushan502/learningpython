from collections import defaultdict, deque

class FirstNonRepeating:
    def __init__(self):
        self.frequency = defaultdict(int)  # Store character frequencies
        self.queue = deque()  # Maintain the order of characters
        self.result = []  # Store the results

    def process_character(self, char):
        # Update character frequency
        self.frequency[char] += 1

        # Add the character to the queue
        self.queue.append(char)

        # Remove characters from the queue until finding a non-repeating character
        while self.queue and self.frequency[self.queue[0]] > 1:
            self.queue.popleft()

        # Append the result to the list
        if self.queue:
            self.result.append(self.queue[0])
        else:
            self.result.append(None)  # Append an empty string if no non-repeating character

    def get_results(self):
        return self.result

# Example usage:
stream = "aabbcccd"

fnp = FirstNonRepeating()

for char in stream:
    fnp.process_character(char)

results = fnp.get_results()
print(results) 