
Feature: Using tabs in my ride functionality
    As a TraWell user
    In order to manage my rides
    I want to use view my rides and their details

    Background:
      Given I am logged in TraWell as private user
      And I chosen "My rides" from navigation bar


    Scenario: View recurrent rides as driver
      When I click on "RECURRENT AS DRIVER" button
      Then I should see only my recurrent rides
      And I have option to edit, delete and view details of each ride


    Scenario: View singular rides as passenger
      When I click on "SINGULAR AS PASSENGER" button
      Then I should see my rides as passenger with option to view details of each ride


    Scenario: View details of ride as passenger
      When I click on "SINGULAR AS PASSENGER" button
      And I click "DETAILS" button of first ride
      Then I should see details of the ride
