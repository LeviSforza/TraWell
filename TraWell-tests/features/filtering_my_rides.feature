Feature: Filtering rides functionality
    As a driver
    In order to better manage my rides
    I want to filter them

    Background:
      Given I am logged in TraWell as private user
      And I chosen "My rides" from navigation bar


    Scenario: Filtering by start date
      When I input "27.11.2022" into Start Date field
      Then I should see only rides with later start date


    Scenario: Filtering by place from
      When I input "Czastary" as place from
      Then I should see only rides from "Czastary"


    Scenario: Filtering by place to
      When I input "Wroclaw" as place to
      Then I should see only rides to "Wrocław"

