from src.main_.someTest.classesTest.Dogs import Dogs as aja
from src.main_.someTest.testScripts.app_test import func

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # playwright
    dog = aja("boo")
    print(dog.__str__())
    print(dog.__int__())
    func(23)
