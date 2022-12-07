Feature: Deleting a review
    As a TraWell user
    In order to manage my reviews
    I want to delete a review

    Background:
      Given I am logged in TraWell as private user
      And I am on profile page of the user I previously reviewed


    Scenario: Delete review
      When I click on delete review button
      Then I should see "Ride deleted successfully" popup
