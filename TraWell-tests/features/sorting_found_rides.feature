Feature: Sorting rides found during search functionality
    As a passenger
    In order to quickly find the best ride
    I want to sort rides

    Background:
      Given I found interesting me rides


    Scenario: Sorting by date: highest first
      When I click on "Sort by" filed
      And I click on "Date: highest first"
      Then I should see rides sorted by date - decreasing


    Scenario: Sorting by date: lowest first
      When I click on "Sort by" filed
      And I click on "Date: lowest first"
      Then I should see rides sorted by date - increasing


    Scenario: Sorting by duration: highest first
      When I click on "Sort by" filed
      And I click on "Duration: highest first"
      Then I should see rides sorted by duration - decreasing


    Scenario: Sorting by duration: lowest first
      When I click on "Sort by" filed
      And I click on "Duration: lowest first"
      Then I should see rides sorted by duration - increasing


  Scenario: Sorting by price: highest first
      When I click on "Sort by" filed
      And I click on "Price: highest first"
      Then I should see rides sorted by price - decreasing


    Scenario: Sorting by price: lowest first
      When I click on "Sort by" filed
      And I click on "Price: lowest first"
      Then I should see rides sorted by price - increasing


    Scenario: Sorting by available seats: highest first
      When I click on "Sort by" filed
      And I click on "Available seats: highest first"
      Then I should see rides sorted by available seats - decreasing


    Scenario: Sorting by available seats: lowest first
      When I click on "Sort by" filed
      And I click on "Available seats: lowest first"
      Then I should see rides sorted by available seats - increasing

