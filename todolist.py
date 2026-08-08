print("--------TO DO LIST--------")

while True:
    print("Choose one of the options:\n1.View tasks\n2.Add task\n3.Remove task\n4.Clear the list\n5.exit")
    serial = int(input("Enter serial number:"))

    match serial:
        case 1:
            with open("todo.txt","r") as f:
                lst = f.read()

                if lst == "" :
                     print("no task has been added yet")

                else:
                     print((lst))


        case 2:
            x = 0
            with open("todo.txt","r") as f:
                 if f.read() == "":
                      x = 0
                 else:
                      f.seek(0)
                      x = 1
                      lines = f.readlines()
                      l = len(lines)
                      line = lines[l-1]
                      s = line.split(".", 1)
                      s_no = int(s[0])


            with open("todo.txt","a") as f:
                 task = input("enter the task you want to add:")
                 task = task.lower()

                 if x == 0:
                      f.write(f"1.{task}")
                 else:
                      f.write(f"\n{s_no+1}.{task}")
            print("task added successfully!")
                      

        case 3:
            with open("todo.txt","r") as f:
                    if f.read()=="":
                         print("no task entered yet")
                         continue 
                    n = int(input("enter the serial number of the task you want to remove:"))
                    f.seek(0)
                    lines = f.readlines()
                    tasks = []
                    for line in lines:
                         s = line.split(".")
                         tasks.append(s[1])
                         
            for i in range(0,len(tasks)):
                 if i+1 == n:
                      tasks.pop(i)

            with open("todo.txt","w") as f:
                 num = 1
                 for task in tasks:
                      f.write(f"{num}.{task}")
                      num += 1
            print("task removed successfully!")


        case 4:
              with open("todo.txt","w") as f:
                   f.write("")

              print("To do list has been cleared.")


        case 5:
              break

        case _: print("invalid number entered")
           

     

                    
                 


                





        
        
