# Pass or Fail Checker
# CODE BY LUCKY

marks = int(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("❌ Invalid marks! Please enter a number between 0 and 100.")
elif marks >= 33:
    print("✅ You Passed!")
else:
    print("❌ You Failed.")

           
