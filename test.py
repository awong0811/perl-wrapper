import subprocess
import json

def get_num():
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

def get_array():
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

def get_num2():
    # Call the Perl script and capture the output
    try:
        result = subprocess.run(
            ['perl', 'test.pl', '--num2'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        ret = json.loads(result.stdout)  # Capture the output and remove any trailing newlines
        return ret
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error occurred: {e.stderr}")

def get_list():
    try:
        # Call the Perl script/module and capture the output
        result = subprocess.run(
            ['perl', 'test.pl', '--list'],
            stdout=subprocess.PIPE,
            text=True
        )
        # Split the output by lines to get the array elements
        ret = json.loads(result.stdout)
        return ret
    except subprocess.CalledProcessError as e:
        raise Exception(f"ERror occured: {e.stderr}")
    
def custom_list(number:int, first:str, second:str, third:str):
    try:
        result = subprocess.run(
            ['perl', 'test.pl', first, second, str(number), third , '--clist'],
            stdout=subprocess.PIPE,
            text=True
        )
        ret = json.loads(result.stdout)
        return ret
    except subprocess.CalledProcessError as e:
        raise Exception(f"ERror occured: {e.stderr}")
    
def get_dictionary():
    try:
        result = subprocess.run(
            ['perl', 'test.pl', '--dict'],
            stdout=subprocess.PIPE,
            text=True
        )
        ret = json.loads(result.stdout)
        return ret
    except subprocess.CalledProcessError as e:
        raise Exception(f"ERror occured: {e.stderr}")

# Example usage
if __name__ == "__main__":
    num = get_num()
    print("Num: ", num, ", Variable type: ", type(num))
    print("Converting string to int: ")
    num = int(num)
    print("Num: ", num, ", Variable type: ", type(num))
    array = get_array()
    print(array)
    num2 = get_num2()
    print("Num2: ", num2, ", Variable type: ", type(num2))
    list = get_list()
    print("List: ", list, ", Variable type: ", type(list))
    list = custom_list(4, 'list', 'with', 'inputs')
    print('Custom List: ', list)
    dict = get_dictionary()
    print(dict)

