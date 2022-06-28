from time import sleep


def imgsrv():

    while True:

        sleep(1)

        # Open file in read/write mode
        with open("image-service.txt", "r+") as image_file:

            # Read file contents
            read_data = image_file.read()

            if read_data.isnumeric():

                # Clear file contents
                image_file.seek(0)
                image_file.truncate()

                # Write random number to file
                image_file.write("CS361/A1/images/" + read_data + ".jpg")


if __name__ == "__main__":
    imgsrv()
