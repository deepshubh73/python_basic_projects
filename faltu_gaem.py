

story = {"Running" : 1,
         "Eating" : 2,
         "Romance" : 3,
         "Travelling" : 4}
print(story)

while True:
    print("Enter 1 to add a new story")
    print("Enter 2 to view all stories")
    print("Enter 3 to search a story")
    print("Enter 4 to delete a story")
    print("Enter 5 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        story_name = input("Enter the story name: ")
        story_number = int(input("Enter the story number: "))
        story[story_name] = story_number
        print("Story added successfully")
    elif choice == 2:
        for story_name, story_number in story.items():
            print(f"{story_name} : {story_number}")
    elif choice == 3:
        story_name = input("Enter the story name: ")
        if story_name in story:
            print(f"{story_name} : {story[story_name]}")
        else:
            print("Story not found")
    elif choice == 4:
        story_name = input("Enter the story name: ")
        if story_name in story:
            del story[story_name]
            print("Story deleted successfully")
        else:
            print("Story not found")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
