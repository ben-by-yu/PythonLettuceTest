Feature: Project Test 1

@GoogleSearch
Scenario: Search Master Chief In Google
	Given I am on google web page
	When I input master chief
	And I click submit
	Then I should see the search result of master chief

@GoogleSearch
Scenario: Search Halo
	Given I am on google web page
	When I input Halo
	And I click submit
	Then I should see the search result of Halo


