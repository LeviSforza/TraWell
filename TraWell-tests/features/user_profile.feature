
Feature: User profile functionality
    As a customer
    In order to manage my data
    I want to have access to my user profile

    Scenario: View profile
      Given I am logged in TraWell
      When I click on "My profile" button in user menu
      Then I should see my user profile

      # pos. tutaj tez recenzje testowac
