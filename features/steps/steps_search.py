# coding=utf-8
# Unicode is important for multi-lingual support

from behave import given, when, then
from hamcrest import *

__author__ = 'ruthlesshelp'


# Google searching
@given(u'I am on the Google homepage')
def step_visit_Google_homepage(context):
    context.session.visit('http://www.google.com/xhtml')

@when(u'I enter "pycabara" in the search box')
def step_enter_pycabara(context):
    # the input name="q"
    context.session.fill_in('q', 'pycabara')

@when(u'I click the Search button')
def step_click_Google_search(context):
    # the button id="gbqfb"
    context.session.click_button('gbqfb')

@then(u'I should see "pycabara" in the results')
def step_should_have_pycabara(context):
    context.session.should_have_content('pycabara')

# Etsy searching
@given(u'I am on the Etsy.com homepage')
def step_visit_Etsy_homepage(context):
    context.session.visit('http://www.etsy.com/')

@when(u'I enter "garnet ring" in the search box')
def step_enter_garnet_ring(context):
    # the input name="search_query"
    context.session.fill_in('search_query', 'garnet ring')

@when(u'I search')
def step_click_Etsy_search(context):
    # the button id="search_submit"
    context.session.click_button('search_submit')

@then(u'I should see "garnet ring" in the results')
def step_should_have_garnet_ring(context):
    context.session.should_have_content('garnet ring')

@then(u'I should see the item count is greater than 1')
def step_should_have_item_count_greater_than(context, expected=1):
    # todo: not implemented
    pass
