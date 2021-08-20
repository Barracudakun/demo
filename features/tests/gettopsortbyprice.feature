# Created by omar at 8/8/2021
Feature: Sort by list feature is working
  #make sure high to low price list is right.
  #make sure low to high price list is right.


  Scenario: Sorting by price and checking the list is correct price ascending order
    Given User URL directly
    #When Click on search by descending
    When Products are displayed in correct order, Sort by price: low to high option is preselected by price
    Then verify price in url
    Then verify price is ascending starts at 379
  Scenario: Sorting by price and checking the list is correct price descending order
    Given User URL directly
    #When Click on search by ascending
    When Products are displayed in correct order, Sort by price: high to low option is preselected by price-desc
    Then verify price-desc in url
    Then verify price-desc is descending starts at 999

