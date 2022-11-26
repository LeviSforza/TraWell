Feature: Filtering rides found during search functionality
    As a passenger
    In order to quickly find the best ride
    I want to filter rides

    Background:
      Given I found interesting me rides


    Scenario: Filtering by start date
      When I input "30.12.2022" into Start Date field
      Then I should see only rides with later start date


    Scenario: Filtering by start time
      When I input "16:00" into Start Time field
      Then I should see only rides with later start time


    Scenario: Filtering by min price
      When I input 10 as min price
      Then I should see only rides with higher price


    Scenario: Filtering by max price
      When I input 40 as max price
      Then I should see only rides with lower price


   Scenario: Filtering by driver review
      When I click on 3 stars
      Then I should see only rides from drivers with 3 stars and more

