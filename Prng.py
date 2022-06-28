from random import randint
from time import sleep


def prng():

    while True:

        sleep(1)

        # Open file in read/write mode
        with open("prng-service.txt", "r+") as prng_file:

            # Read file contents
            read_data = prng_file.read()

            if read_data == "run":

                # Clear file contents
                prng_file.seek(0)
                prng_file.truncate()

                # Generate random number
                index = str(randint(1, 5))

                # Write random number to file
                prng_file.write(index)


if __name__ == "__main__":
    prng()
