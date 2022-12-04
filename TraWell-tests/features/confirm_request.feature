Feature: Confirm a join request
    As a TraWell user
    In order manage passengers
    I want to accept or decline join requests

    Background:
      Given I am logged in TraWell as private passenger
      And I am on pending requests view


    Scenario: Accept a request
      When I click on "Accept" button
      And I click on confirmation
      Then I shouldn't see request on pending page anymore


    Scenario: Decline a request
      When I click on "Decline" button
      And I click on confirmation
      And I click on "Okay" button to close popup
      Then I shouldn't see request on pending page anymore
