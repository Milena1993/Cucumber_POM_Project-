from utilities.conftest import setup, config
from pages.delete_user import DeleteUser
from pages.login_page import LoginPage
from pages.add_user import AddUser
from pages.search_user import CustomerPage
from pytest_bdd import scenario, given, when, then
import pytest
import time


@scenario('../features/cucumber.feature', 'As a bank manager, I can add and delete customer')
@given("I'm on XYZ Bank login Page")
def test_add_customer_flow(setup):
    login_page = LoginPage(setup)
    login_page.get_page_title()


@then("I assert that I'm on XYZ Bank login Page")
def page_check(setup):
    login_page = LoginPage(setup)
    expected_result = login_page.page_title
    assert login_page.get_page_title() == expected_result


@when("I login as a bank manager by clicking on Add Customer button")
def login(setup):
    login_page = LoginPage(setup)
    login_page.bank_manager_login()


@when("I fill up all the required fields")
def add_customer(setup):
    global name, last_name, postal_code
    add_user = AddUser(setup)
    name = add_user.add_customer_firstname()
    last_name = add_user.add_customer_lastname()
    postal_code = add_user.add_customer_postcode()


@when("I click on Add Customer button")
def submit_customer(setup):
    add_user = AddUser(setup)
    add_user.submit_new_customer()


@when("I search the new created customer by firstname")
def search_customer(setup):
    customer_page = CustomerPage(setup)
    customer_page.search_customers(name)


@then("I assert that the customer is added with correct info") 
def customer_info_check(setup):
    customer_page = CustomerPage(setup)
    assert customer_page.search_customers(name) == customer_page.table_firstname()
    assert last_name == customer_page.table_lastname()
    assert postal_code == customer_page.table_postcode()


@when("I delete the customer by clicking on Delete button")
def delete_user(setup):
    delete_user = DeleteUser(setup)
    delete_user.delete_customer()


@then("I assert that the customer information is deleted")
def deleted_customer_check(setup):
    delete_user = DeleteUser(setup)
    assert delete_user.table_existing_check() == False

