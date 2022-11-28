Feature: Sorting my rides functionality
    As a driver
    In order to better manage my rides
    I want to sort them

    Background:
      Given I am logged in TraWell as private user
      And I chosen "My rides" from navigation bar


    Scenario: Sorting by date: highest first
      When I click on "Sort by" filed
      And I click on "Date: highest first"
      Then I should see my rides sorted by date decreasing


    Scenario: Sorting by date: lowest first
      When I click on "Sort by" filed
      And I click on "Date: lowest first"
      Then I should see my rides sorted by date increasing


    Scenario: Sorting by duration: highest first
      When I click on "Sort by" filed
      And I click on "Duration: highest first"
      Then I should see my rides sorted by duration decreasing


    Scenario: Sorting by duration: lowest first
      When I click on "Sort by" filed
      And I click on "Duration: lowest first"
      Then I should see my rides sorted by duration increasing
