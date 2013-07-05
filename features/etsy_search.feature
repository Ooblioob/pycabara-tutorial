# As a <type of user> I want <some goal> so that <some reason>
Feature: Search the Etsy.com inventory
  As a potential customer
  I want to search for an item
  So that I can view the available products

@smoke_test
Scenario: Basic search for "garnet ring"
	Given I am on the Etsy.com homepage
	When I enter "garnet ring" in the search box
	And I search
	Then I should see "garnet ring" in the results
	And I should see the item count is greater than 1

@ignore
Scenario: Advanced search for a hat
    Given I am on the Etsy.com homepage
    When I specify the "Knitting" sub category
    And I search for "hat"
    Then I should see search results

@ignore
Scenario: Advanced search for a ring
    Given I am on the Etsy.com homepage
    When I specify the "Jewelry" sub category
    And I search for "ring"
    Then I should see search results
