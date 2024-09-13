import subprocess

def get_array_from_perl():
    try:
        # Call the Perl script/module and capture the output
        result = subprocess.run(
            ['perl', 'test.pl', '--array'],
            stdout=subprocess.PIPE,
            text=True
        )

        # Split the output by lines to get the array elements
        array = result.stdout.strip().split(' ')
        
        return array
    except subprocess.CalledProcessError as e:
        raise Exception(f"ERror occured: {e.stderr}")

def foo():
    # Call the Perl script and capture the output
    try:
        result = subprocess.run(
            ['perl', 'test.pl', '--num'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        dx = result.stdout.strip()  # Capture the output and remove any trailing newlines
        return dx
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error occurred: {e.stderr}")

# Example usage
if __name__ == "__main__":
    num = foo()
    print("Num: ", num, ", Variable type: ", type(num))
    print("Converting string to int: ")
    num = int(num)
    print("Num: ", num, ", Variable type: ", type(num))
    array = get_array_from_perl()
    print(array)