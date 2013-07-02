# coding=utf-8
# Unicode is important for multi-lingual support

from behave import given, when, then
from hamcrest import *

__author__ = 'ruthlesshelp'


@given(u'I am on the Google homepage')
def step_visit_homepage(context):
    context.session.visit('http://www.google.com/xhtml')

@when(u'I enter "pycabara" in the search box')
def step_enter_pycabara(context):
    # the input name="q"
    context.session.fill_in('q', 'pycabara')

@when(u'click the Search button')
def step_click_search(context):
    # the button id="gbqfb"
    context.session.click_button('gbqfb')

@then(u'I should see "pycabara" the results')
def step_should_have_pycabara(context):
    context.session.should_have_content('pycabara')
