import time

flag = "fl" + "ag{" + "byp4ss_" + "1nf1n1t3}"
while True:
    user_input = input("Enter the secret code: ")
    if user_input[::-1] == "tuo em tel":  # Reverse condition (tricky!)
        print("Correct! The flag is:", flag)
        break
    time.sleep(1)
