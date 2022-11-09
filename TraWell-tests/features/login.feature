
Feature: Login functionality
    As a customer
    In order to use the TraWell application
    I want to login with email and password

    Background:
      Given I am on the login page
      And the field 'Email' is empty
      And the field 'Password' is empty

    Scenario: Error on empty fields
      When I click on 'SIGN IN'
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


  Scenario: Login with Google SSO
    # ????
