#
#Feature: Creating account functionality
#    As a customer
#    In order to use all functionalities of the TraWell application
#    I want to create user account
#
#    Scenario: Registering new user
#      Given I am on the login page
#      When I click on 'Register'
#      Then I should see 'Register' form
#
#    Scenario: Error on empty fields
#      Given I am on register page
#      When I click on 'SIGN IN'
#      Then I should see 'Please specify this field.' under: 'Email', 'First Name', 'Last Name', 'Account Type', 'Date of birth'
#
#
#    Scenario: Error on invalid email
#      Given I am on register page
#      When I type 'anna' in 'Email'
#      And I click on 'SIGN IN'
#      Then I should see 'Invalid email address.'
#
#
#    Scenario: Error on incorrect password confirmation
#      Given I am on register page
#      When I type '123' in 'Password'
#      When I type 'abc' in 'Confirm Password'
#      And I click on 'SIGN IN'
#      Then I should see 'Password confirmation doesn't match.'
#
#
#    Scenario: Error on invalid date of birth
#      Given I am on register page
#      When I type 'dd.09.rrrr' in 'Date of birth'
#      And I click on 'SIGN IN'
#      Then I should stay on register page
#      And my mouse should be focused on 'Date of birth' field
#
#
#    Scenario: Error on invalid Facebook URL
#      Given I am on register page
#      When I type 'rand_string' in 'Facebook'
#      And I click on 'SIGN IN'
#      Then I should stay on register page
#      And my mouse should be focused on 'Facebook' field
#
#    Scenario: Error on invalid Instagram URL
#      Given I am on register page
#      When I type 'rand_string' in 'Instagram'
#      And I click on 'SIGN IN'
#      Then I should stay on register page
#      And my mouse should be focused on 'Instagram' field
#
#    Scenario: Register successfully
#        Given I am on register page
#        When I type 'anna@mak.com' in 'Email'
#        And I type 'Anna' in 'First Name'
#        And I type 'Mak' in 'Last Name'
#        And I type 'good_pass' in 'Password'
#        And I type 'good_pass' in 'Confirm Password'
#        And I input 'Private User' in 'Account Type'
#        And I input '01.01.1999' in 'Date of birth'
#        And I click on 'SIGN IN'
#        Then I should see prompt 'Email Verification'
#
#
