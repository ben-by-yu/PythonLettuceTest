Feature: Project Test 2

@OutlookLogin
Scenario: Login Outlook
	Given I am on outlook web page
	When I input login and password
		|login					|password	|

	Then I should see inbox
