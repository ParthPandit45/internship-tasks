import os

def main():
    print("Simple To-Do List")
    print("1. Add a new task")
    print("2. View all tasks")
    
    choice = input("Choose an option (1 or 2): ")
    
    if choice == "1":
        try:
            # Opening the file
            file = open(filename, "a")
            new_task = input("What do you need to do? ")
            
            # Writing to the file
            file.write(new_task + "\n")
            print("Task saved successfully!")
            
        except IOError as e:
            # Exception handling
            print(f"An error occurred while saving the file: {e}")
            
        finally:
            # Closing the file
            if 'file' in locals():
                file.close()
                
    elif choice == "2":
        try:
            # Opening the file
            file = open(filename, "r")
            
            tasks = file.readlines()
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task.strip()}")
                    
        except FileNotFoundError:
            # Exception handling specifically for missing files
            print("No tasks found. Try adding one first!")
        except Exception as e:
            # Catch-all exception handling
            print(f"An unexpected error occurred: {e}")
            
        finally:
            # Closing the file
            if 'file' in locals():
                file.close()
                
    else:
        print("Invalid option. Please run the script again.")

if __name__ == "__main__":
    main()
