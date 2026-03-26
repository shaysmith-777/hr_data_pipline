#Opening the files and reading the data into a list
obj = open("data/phase0.text", "r")
hr_data_phase0 = obj.readlines()
print(hr_data_phase0)

#Removing "/n" from the list and converting strings into integers
for x in hr_data_phase0:
  new_hr_data_phase0 = [int(x.strip("\n"))]
print(new_hr_data_phase0)

#Now since I have a list of integers, I need to remove none values and outliers.
#Also realizing that I have floats in the data, typcasting those as well.
def clean_hr_data_phase0(data: new_hr_data_phase0) -> tuple:
    cleaned = []
    for x in data:
        data = int(float(x))
        if x == None:
            continue
        cleaned.append(data)
    return tuple(cleaned)

print(clean_hr_data_phase0)
#def clean_heartrate_data(data: list) -> tuple:
 
 # I tried to make a list without realizing first I need to open the file  

#raw_heart_data0 = [69, 75, 84, 79, 72, 69, 93, 91, 72, 76, 69, 71, 60, 63, 67, 58, 63, 61, 65, 66, 62]
#newraw_heart_data0 = tuple(raw_heart_data)
#print(newraw_heart_data0)

    Clean raw heart-rate data by removing malformed or impossible values.

#Reading this realizing I wasn't supposed to clean the data...yet. I will still write the function.

#def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
def average(data: new_hr_data_phase0) -> float:
    sum = 0
    for i  in range(len(data)):
        sum += data[i]
        average = sum / len(data)
    print(average)
        

#Finding the median of the data
#def median(data: list) -> float:
    """
    """
def median(data: new_hr_data_phase0) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    print(median)

#Finding the range of the data
#def range(data: list) -> float:
    """
    """
def range(data: new_hr_data_phase0) -> float:
    range = max(data) - min(data)
    print(range)


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass
#Defining a function to run the data pipeline
#def run(file: str):
    """
def run(obj: "data/phase0.txt"):
    
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    #data = []

    # open file using file I/O and read it into the `data` list
# This was not in order or proper formatted so I added hashtags so the computer would not read this.

#def readlines in file:
#file = open("data/phase0.txt", "r")
#data = file.readlines()

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = ...

    # calculate the average, median, and range of this file using the functions you've wrote
    ...

    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
