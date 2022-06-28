from time import sleep


def ui():

    while True:

        # Get user input
        user_input = input("Enter 1 to generate a new image or 2 to exit: ")

        if user_input == "1":

            # Global variables
            index = ""
            path = ""

            with open("prng-service.txt", "r+") as prng_file:

                # Clear file contents
                prng_file.seek(0)
                prng_file.truncate()

                # Write "run" to file
                prng_file.write("run")

            # Wait for program to execute
            sleep(5)

            with open("prng-service.txt", "r+") as prng_file:

                # Read random number from file
                prng_file.seek(0)
                index = prng_file.read()

            # Open image service file in read/write mode
            with open("image-service.txt", "r+") as image_file:

                # Clear file contents
                image_file.seek(0)
                image_file.truncate()

                # Write random number to file
                image_file.write(index)

            # Wait for program to execute
            sleep(5)

            # Open image service file in read/write mode
            with open("image-service.txt", "r+") as image_file:

                # Read image path from file contents
                image_file.seek(0)
                path = image_file.read()

            print("image path: ", path, "\n")

        elif user_input == "2":

            print("exiting...\n")

            return

        else:

            print("unknown option...\n")


if __name__ == "__main__":
    ui()
