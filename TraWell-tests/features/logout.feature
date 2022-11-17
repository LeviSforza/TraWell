
Feature: Logout functionality
    As a customer
    In order to guarantee safety of my personal data
    I want to logout from TraWell application

    Scenario: Logout successfully
      Given I am logged in TraWell
      When I click on "Log out" button in user menu
      Then I should see "LOGIN" button in navigation bar
      And I should be on the login page
