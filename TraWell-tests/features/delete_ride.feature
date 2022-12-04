
Feature: Deleting a ride functionality
    As a TraWell user
    In order to manage my rides
    I want to delete a ride

    Background:
      Given I am logged in TraWell as private user
      And I am on my rides page


    Scenario: Delete singular rides
      When I click on "SINGULAR" button
      When I click on "ADD RIDE" button
      Then I should see error message "You have to choose starting place - "Place from""

