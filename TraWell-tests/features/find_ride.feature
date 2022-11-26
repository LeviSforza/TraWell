Feature: Finding a ride functionality
    As a passenger
    In order to find a ride
    I want to search for interesting me rides

    Background:
      Given I am on TraWell homepage


    Scenario: Error on empty fields
      When I click on "FIND" button
      Then I should see error "All fields are obligatory. Please fill them"


    Scenario: Search successfully and rides found
      When I input "Katowice" as starting place
      And I input "Wrocław" as destination
      And I input "24.12.2022" as date of the ride
      And I input "10:00" as time of the ride
      And I input "2" as amount of passengers
      And I click on "FIND" button
      Then I should see summary of search parameters
      And rides consistent with search


    Scenario: Search successfully but no rides found
      When I input "Gdynia" as starting place
      And I input "Leszno" as destination
      And I click on "FIND" button
      Then I should see summary of search parameters
      And I should see "No rides found from: Gdynia to Leszno" message
