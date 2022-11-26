
Feature: Setting up account functionality
    As a guest
    In order to use all functionalities of the TraWell application
    I want to create user account

    Scenario: Registering new user
      Given I am on the login page
      When I click on "Register"
      Then I should see Register form

    Scenario: Error on empty fields
      Given I am on register page
      When I click on "Register" button
      Then I should see "Please specify email." under "Email"
      And I should see "Please specify password." under "Password"
      And I should see "Please specify this field." under "First Name", "Last Name", "Account Type", "Date of birth"


    Scenario: Error on invalid email
      Given I am on register page
      When I type "abcd" in Email field
      When I click on "Register" button
      Then I should see "Invalid email address." under "Email"


    Scenario: Error on incorrect password confirmation
      Given I am on register page
      When I type "123" in Password field
      When I type "abc" in Password-Confirm field
     When I click on "Register" button
      Then I should see "Password confirmation doesn't match." under "Confirm password"


    Scenario: Error on invalid date of birth
      Given I am on register page
      When I type "dd.09.rrrr" in Date of birth field
      When I click on "Register" button
      Then I should stay on register page
      And my mouse should be focused on Date of birth field


    Scenario: Error on invalid Facebook URL
      Given I am on register page
      When I type "abcd" in Facebook field
      When I click on "Register" button
      Then I should stay on register page
      And my mouse should be focused on Facebook field

    Scenario: Error on invalid Instagram URL
      Given I am on register page
      When I type "abcd" in Instagram field
      When I click on "Register" button
      Then I should stay on register page
      And my mouse should be focused on Instagram field

    Scenario: Register successfully
        Given I am on register page
        When I type "anna@mak.com" in Email field
        And I input "Anna" in First Name field
        And I input "Mak" in Last Name field
        And I type "good_pass" in Password field
        And I type "good_pass" in Password-Confirm field
        And I type "Private User" in User Type field
        And I type "01.01.1999" in Date of birth field
        When I click on "Register" button
        Then I should see Email verification form


