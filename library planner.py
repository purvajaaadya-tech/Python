print("=== Library Visit Planner ===")
print ("Answer 3 quick questions and i will plan your library visit!\n")

day = input("What day is it? (monday to sunday): ").strip().lower()

weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()

book_due = input("Do you have a book to return? (yes / no): ").strip().lower()

print()
print(f"=== Your Library Plan for {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day type: Weekend - a good time for a relaxed library visit!")

elif day == "Monday":
    print("Day type: Start of the week - check your reading list!")

elif day == "Friday":
    print("Day type: Last school day - return books before weekend!")

elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type: Regular school day - plan a short library visit!")

else:
    print("Day type: Day not recognised - please check the spelling!")

if weather == "sunny" and book_due == "yes":
    print("Library tip: Great weather - return your book and borrow a new one!")

if weather == "rainy" or weather == "cloudy":
    print("Library tip: It may rain - carry an umbrella if you are going to the library!")

if not (book_due == "yes"):
    print("Book status: No book return needed today - you can browse new books!")

if weather == "rainy" and book_due == "yes":
    print("Best plan: Vist the library carefully - return your book on time!")

elif weather == "sunny" and book_due == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan: Stop by the library after school - return your book!")

elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan: Perfect day - longer reading reading session at the library!")

else:
    print("Best plan: Check your schedule - plan a simple library visit!")

print()
print("Library plan complete! Happy reading!")