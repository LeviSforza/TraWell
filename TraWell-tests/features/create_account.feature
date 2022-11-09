
Feature: Creating account functionality
    As a customer
    In order to use all functionalities of the TraWell application
    I want to create user account

    Background:
      Given I am on the login page

    Scenario: Registering new user
      When I click on 'Register'
      Then I should see prompt 'Invalid username or password.'

    Scenario: Wrong password
      When I type 'olga@tokarczuk.com' in 'Email'
      And I type 'wrong_pass' in 'Password'
      And I click on 'SIGN IN'
      Then I should see prompt 'Invalid username or password.'

  Scenario: Login successfully
    Given I have users:
      | name           | email              | password     |
      | Olga Tokarczuk | olga@tokarczuk.com | correct_pass |
    When I type 'olga@tokarczuk.com' in 'Email'
    And I type 'correct_pass' in 'Password'
    And I click on 'SIGN IN'
    Then I should be on the users home page
    And I shouldn't see 'LOGIN' button

