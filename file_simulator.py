# importing module
import time

if __name__ == "__main__":

    path = "./synthetic_files"

    i = 0
    while True:
        # Creates a new file
        i += 1
        file_name = f"test02{i}"
        with open(f"{path}{file_name}.txt", "w") as fp:
            pass
        time.sleep(10)
