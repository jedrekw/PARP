# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import rstr
from ExtendedSelenium2Library import ExtendedSelenium2Library
from random import randint
import uuid
import datetime

class page(ExtendedSelenium2Library):
    # def __init__(self, driver=None, title=None, url=None):
    #     self._driver = driver
    #     self._title = title
    #     self._url = url

    def get_driver(self):
        return self._current_browser()

    def get_random_string(self, length=8):
        return rstr.rstr("abcdefghijklmnoprstuwxyz", length)

    def get_random_string_1_char(self):
        return self.get_random_string(1)

    def get_random_string_big_letters(self, length=8):
        return rstr.rstr("ABCDEFGHIJKLMNOPRSTUWXYZ", length)

    def get_random_password(self):
        return str(self.get_random_integer(2)+self.get_random_string(4)+self.get_random_string_big_letters(4)+"$")

    def get_random_integer(self, length=6):
        range_start = 10**(length-1)
        range_end = (10**length)-1
        return str(randint(range_start, range_end))

    def get_random_integer_1_char(self):
        return str(self.get_random_integer(1))

    def get_random_integer_0_1(self):
        return randint(0, 1)

    def get_random_integer_1_2(self):
        return randint(1, 2)

    def get_random_integer_in_range_2_x(self, max=2):
        return "["+str(randint(2, int(max)))+"]"

    def get_random_integer_8_chars(self):
        return str(self.get_random_integer(8))

    def get_random_integer_10_chars(self):
        return self.get_random_integer(10)

    def get_random_integer_devided(self):
        return self.get_random_integer(1)+"/"+self.get_random_integer(1)

    def get_random_floating_point(self, length=2):
        return str(self.get_random_integer(length)+"."+self.get_random_integer(2))

    def get_random_floating_point_milions(self):
        return self.get_random_floating_point(8)

    def get_random_floating_point_milion(self):
        return self.get_random_floating_point(7)

    def get_random_pesel(self):
        a = randint(0, 9)
        b = randint(0, 9)
        c = 0
        d = randint(0, 9)
        e = 0
        f = randint(0, 9)
        g = randint(0, 9)
        h = randint(0, 9)
        i = randint(0, 9)
        j = randint(0, 9)
        k = (9*a+7*b+1*d+7*f+3*g+1*h+9*i+7*j) % 10
        return str(a)+str(b)+"0"+str(d)+"0"+str(f)+str(g)+str(h)+str(i)+str(j)+str(k)

    def get_random_nip(self):
        a = randint(0, 9)
        b = randint(0, 9)
        c = randint(0, 9)
        d = randint(0, 9)
        e = randint(0, 9)
        f = randint(0, 9)
        g = randint(0, 9)
        h = randint(0, 9)
        i = randint(0, 9)
        j = (6*a+5*b+7*c+2*d+3*e+4*f+5*g+6*h+7*i) % 11
        if j==10:
            i = i+1
            j = (6*a+5*b+7*c+2*d+3*e+4*f+5*g+6*h+7*i) % 11
        return str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)[:1]

    def get_random_regon(self):
        a = randint(0, 9)
        b = randint(0, 9)
        c = randint(0, 9)
        d = randint(0, 9)
        e = randint(0, 9)
        f = randint(0, 9)
        g = randint(0, 9)
        h = randint(0, 9)
        j = (8*a+9*b+2*c+3*d+4*e+5*f+6*g+7*h) % 11
        if j == 10:
            j = 0
        return str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(j)

    def get_random_uuid(self, length=5):
        return str(uuid.uuid1())[:length]

    def get_random_email(self):
        return str(self.get_random_uuid(9) + "@wp.pl")

    def get_todays_date(self):
        _today = datetime.date.today()
        return _today.strftime('%Y-%m-%d')

    def get_random_date(self):
        y = str(randint(2000, 2016))
        m = str(randint(10, 12))
        d = str(randint(10, 29))
        return y+"-"+m+"-"+d

    def get_random_postal_code(self):
        return str(randint(10, 99))+"-"+str(randint(100, 999))

    def cut_last_char_from_string(self, string):
        return string[:-1]

    def type_of_variable(self, var):
        return type(var)

    def get_tomorrows_date(self):
        _tommorow = datetime.date.today()+ datetime.timedelta(days=1)
        return _tommorow.strftime('%Y-%m-%d')

    def get_2_days_ahead_date(self):
        _2_days_ahead = datetime.date.today()+ datetime.timedelta(days=2)
        return _2_days_ahead.strftime('%Y-%m-%d')
