# As a <type of user> I want <some goal> so that <some reason>
Feature: Search with Google through the pycabara testing tool
  As a person who enjoys trivia
  I want to use Google to search for a keyword
  So that I can read good references that relate to the topic

@smoke_test
Scenario: Basic search for "pycabara"
	Given I am on the Google homepage
	When I enter "pycabara" in the search box
	And I click the Search button
	Then I should see "pycabara" in the results
