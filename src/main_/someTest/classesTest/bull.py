import puppy as pup
import puppyBoo as boo
import src.main_.base.capabilities
import src.main_.drivers.DriverManager as driver
from src.main_.drivers.DriverManager import __str__
from src.main_.someTest.classesTest.Dogs import Dogs
from datetime import datetime, date


class Bull(Dogs):

    def __init__(self):
        super().__init__(boo.name)
        self.name = boo.name
        self.last_name = pup.name
        self.driver = __str__()
        self.date = datetime.date()
        self.date_ = date.today()
        self.day = datetime(2023, 6, 14).day
        self.month = datetime(2023, 6, 14).month
        self.year = datetime(2023, 6, 14).year

    def __str__(self):
        return boo.name
