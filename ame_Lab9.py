def encode(password):
	encode = ""
	for num in password:
		encode += str(int(num) + 3)
	return encode

def main():
	global password
	while True:
		print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
		choice = input("Enter an option: ")

		if choice == "1":
			password = input("Please enter your password to encode: ")
			print("Your password has been encoded and stored!")

		if choice == "2":
			print(f"The encoded password is {encode(password)} , and the original password is {password}")

		if choice == 3:
			break

if __name__ == "__main__":
	main()
