stack = []

# Push operations
stack.append("Quiz1")
stack.append("Quiz2")
stack.append("Quiz3")

# Undo two times (pop twice)
stack.pop()  # Removes Quiz3
stack.pop()  # Removes Quiz2

# Top of stack
top = stack[-1]
print("Top of Stack is:", top)
# Output: Top of Stack is: Quiz1
stack = []

# Push operations
stack.append("Upload ID")
stack.append("Fill Form")
stack.append("Submit")

# Undo one (pop once)
stack.pop()  # Removes "Submit"

# Top of stack
top = stack[-1]
print("Top of Stack is:", top)
# Output: Top of Stack is: Fill Form
stack = []

# Push operations
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")

# Pop one (remove "4")
stack.pop()

# Push "5"
stack.append("5")

# Top of stack
top = stack[-1]
print("Top of Stack is:", top)
# Output: Top of Stack is: 5
from collections import deque

# Queue operations
queue = deque(["C1", "C2", "C3", "C4", "C5", "C6"])

# Serve (dequeue) two clients
queue.popleft()  # Removes C1
queue.popleft()  # Removes C2

# Front of the queue
front = queue[0]
print("Client at the front is:", front)
# Output: Client at the front is: C3
from collections import deque

# Queue operations
queue = deque(["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"])

# Serve all patients
last_served = None
while queue:
    last_served = queue.popleft()

print("The last patient served is:", last_served)
# Output: The last patient served is: P8

