Feature: Adding a review
    As a TraWell user
    In order to rate other users
    I want to add a review

    Background:
      Given I am logged in TraWell as private user
      And I am on profile page of the user I want to rate


    Scenario: Add ride without description
      When I click on "Add review" button
      And I click on "ADD RIDE" button
      Then I should see error message "You have to choose starting place - "Place from""


    Scenario: Add ride with description
      When I click on "RECURRENT" button
      When I click on recurrent "ADD RIDE" button
      Then I should see error message "You have to choose starting place - "Place from""


    Scenario: Post singular ride (mandatory fields) successfully
      When I click on "SINGULAR" button
      And I input "Katowice" as City from
      And I input "Leszno" as City to
      And I input "23/11/2023" as Start date of the ride
      And I input "16:21" as Start time of the ride
      And I input "2" hours as duration of ride
      And I input "35" minutes as additional duration of ride
      And I input "12.99" as Price for the ride
      And I choose first vehicle from list
      When I click on "ADD RIDE" button
      Then I should see "Ride added successfully" modal
      When I click on "OKAY" button
      Then I should be on home page
