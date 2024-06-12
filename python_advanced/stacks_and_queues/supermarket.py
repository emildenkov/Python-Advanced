from collections import deque

input_text = input()
clients = deque()

while input_text != "End":
    if input_text == "Paid":
        while clients:
            print(clients.popleft())
    else:
        clients.append(input_text)

    input_text = input()

print(f"{len(clients)} people remaining.")
