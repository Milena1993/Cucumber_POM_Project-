Feature: Add Customer
    Scenario: As a bank manager, I can add and delete customer
        Given I'm on XYZ Bank login Page
        Then I assert that I'm on XYZ Bank login Page
        When I login as a bank manager by clicking on Add Customer button
        And I fill up all the required fields 
        And I click on Add Customer button
        When I search the new created customer by firstname
        Then I assert that the customer is added with correct info
        When I delete the customer by clicking on Delete button
        Then I assert that the customer information is deleted
