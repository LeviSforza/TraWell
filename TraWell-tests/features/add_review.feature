Feature: Adding a review
    As a TraWell user
    In order to rate other users
    I want to add a review

    Background:
      Given I am logged in TraWell as private user
      And I am on profile page of the user I want to rate


    Scenario: Add ride without description and default ride
      When I click on "Add review" button
      And I set rating as 4 stars
      And I click on "Add" button
      Then I should see "Review added successfully" popup


    Scenario: Add ride without description and chosen ride
      When I click on "Add review" button
      And I choose ride from list
      And I set rating as 2 stars
      And I click on "Add" button
      Then I should see "Review added successfully" popup


    Scenario: Add ride with description and default ride
      When I click on "Add review" button
      And I set rating as 4 stars
      And I add description
      And I click on "Add" button
      Then I should see "Review added successfully" popup


