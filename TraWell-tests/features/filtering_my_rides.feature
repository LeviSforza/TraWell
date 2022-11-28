Feature: Filtering rides functionality
    As a driver
    In order to better manage my rides
    I want to filter them

    Background:
      Given I am logged in TraWell as private user
      And I chosen "My rides" from navigation bar


    Scenario: Filtering by start date
      When I input "30.11.2022" as Start Date field
      Then I should see rides with later start date

