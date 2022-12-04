Feature: Book a ride
    As a TraWell user
    In order to join a ride
    I want to send request to book a ride

    Background:
      Given I am logged in TraWell as private user
      And I found rides from "Katowice" to "Wrocław"


    Scenario: Book a ride
      When I click on found ride
      And I click on "Book ride" button
      And I click "Yes" to confirm booking
      Then I should see "Book ride" popup info


    Scenario: Book a ride for multiple seats
      When I click on second found ride
      And I set number of seats to "2"
      And I click on "Book ride" button
      And I click "Yes" to confirm booking
      Then I should see "Book ride" popup info