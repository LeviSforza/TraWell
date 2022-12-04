
Feature: Posting a ride functionality
    As a TraWell user
    In order to find passengers
    I want to post a ride

    Background:
      Given I am logged in TraWell as private user
      And I chosen "Post a ride" from navigation bar


    Scenario: Error on all empty fields on singular rides
      When I click on "SINGULAR" button
      When I click on "ADD RIDE" button
      Then I should see error message "You have to choose starting place - "Place from""


    Scenario: Error on all empty fields on recurrent rides
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


   Scenario: Post singular ride (all fields) successfully
      When I click on "SINGULAR" button
      And I input "Czastary" as City from
      And I input "ulica Radosna 4" as Exact place from
      And I input "Leszno" as City to
      And I input "Parking obok baru Oliwka" as Exact place to
      And I input "23/11/2023" as Start date of the ride
      And I input "16:21" as Start time of the ride
      And I input "4" as amount of people
      And I input "2" hours as duration of ride
      And I input "35" minutes as additional duration of ride
      And I input "12.99" as Price for the ride
      And I choose first vehicle from list
      When I click on "ADD RIDE" button
      Then I should see "Ride added successfully" modal
      When I click on "OKAY" button
      Then I should be on home page


   Scenario: Post recurrent ride (mandatory fields) successfully
      When I click on "RECURRENT" button
      And I input "Czastary" as City from
      And I input "Bydgoszcz" as City to
      And I input "12.99" as Price
      And I choose first vehicle from list
      And I input "10/12/2023" as Start date
      And I input "30/12/2023" as End date of the ride
      And I input "18:20" as Start time
      And I input "2" hours as duration
      And I click on recurrent "ADD RIDE" button
      Then I should see "Ride added successfully" modal
      When I click on "OKAY" button
      Then I should be on home page


   Scenario: Post recurrent ride (all fields) successfully
      When I click on "RECURRENT" button
      And I input "Czastary, Czastary, Łódź Voivodeship, Poland" as City from
      And I input "ulica Radosna 4" as Exact place from
      And I input "Leszno, Leszno, Greater Poland Voivodeship, Poland" as City to
      And I input "Parking next to Oliwka bar" as Exact place to
      And I choose first vehicle from list
      And I input "53.99" as Price
      And I input "23/11/2023" as Start date
      And I input "31/11/2023" as End date of the ride
      And I input "16:21" as Start time
      And I input "6" as amount of people
      And I input "2" hours as duration
      And I input "35" minutes as additional duration
      And I input "12.99" as Price
      And I choose "Daily" as Frequency type
      And I input "3" as Frequence
      When I click on recurrent "ADD RIDE" button
      Then I should see "Ride added successfully" modal
      When I click on "OKAY" button
      Then I should be on home page


#  Scenario: Edit singular ride
#
#  Scenario: Delete singular ride



#      add scenarios for company user