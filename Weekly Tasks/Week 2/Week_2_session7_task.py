from pathlib import Path

# Define the directory path
folder_path = Path("./my_data_folder")

# Loop through all .txt files in the folder
all_contents = []
for file_path in folder_path.glob("*.txt"):
    if file_path.is_file():
        with open(file_path, "r", encoding="utf-8") as file:
            all_contents.append(file.read())

print(f"Successfully read {len(all_contents)} files!")



user_input = int(input(
    " \n **** Welcome to the Student Management System **** \n\n " 
    "  please select from the following options: \n\n"
    "1: New Admission \n" 
    "2: Attendence Status \n" 
    "3: Exams and Grade Status \n"
    "4: Course Selection \n"
    "5: Fee Record: \n"
    ))

while True:
    if user_input == 1:
        print ("user select New Admission")
    elif user_input == 2:
        print ("user select New Admission")
    elif user_input == 3:
        print ("user select New Admission")
    elif user_input == 4:
        print ("user select New Admission")
    elif user_input == 5:
        print ("user select New Admission")
    else:
        print ("please select the right option from 1 to 5")



scored = [70,80,90,100,110]
mean = sum(scored) / len(scored)

print (mean)
median = sorted (scored) [2]
print(median)