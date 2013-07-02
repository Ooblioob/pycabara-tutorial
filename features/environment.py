import time
from selenium import webdriver
from pycabara.Element import Element
from pycabara.Session import Session

__author__ = 'ruthlesshelp'


def before_all(context):
    context.session = Session(':selenium')


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    context.session.driver.quit()
