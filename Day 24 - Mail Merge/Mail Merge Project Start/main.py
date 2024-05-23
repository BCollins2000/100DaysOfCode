#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



names = open(r"C:\Users\U358530\Desktop\100DaysOfCode\Day 24 - Mail Merge\Mail Merge Project Start\Input\Names\invited_names.txt", "r")
name_list = names.read().splitlines()
names.close()


print(name_list)

for name in name_list:
    template = open(r"C:\Users\U358530\Desktop\100DaysOfCode\Day 24 - Mail Merge\Mail Merge Project Start\Output\ReadyToSend\example.txt", "r")
    text = template.read()
    text = text.replace("_name_here_", name)
    #print(text)
    template.close
    base_path = r"C:\Users\U358530\Desktop\100DaysOfCode\Day 24 - Mail Merge\Mail Merge Project Start\Output\ReadyToSend"
    file_name = f"{name}_letter.txt"
    file_path = base_path  + "\\" + file_name
    with open(file_path, "w") as file:
        file.write(text)



