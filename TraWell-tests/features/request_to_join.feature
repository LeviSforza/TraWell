#Feature: Requesting to join a ride functionality
#    As a passenger
#    In order to join a ride
#    I want to request to join selected ride
#
#    Background:
#      Given I searched for interesting me rides
#      And I click first found ride
#
#
#    Scenario: Resign from requesting to join
#      When I click on "BOOK RIDE" button
#      And I click "NO" button
#      Then popup disappears
#
#
#    Scenario: Request to join successfully
#      When I click on "BOOK RIDE" button
#      And I click "YES" button
#      Then I should see "Request successfully sent" message
#      When I click "OKAY" button
#      Then popup disappears
#
