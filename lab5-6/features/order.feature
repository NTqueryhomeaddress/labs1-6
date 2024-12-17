Feature: Order Processing

  Scenario: Process Physical Order
    Given a physical order factory
    When I create a physical order
    Then the result should be "Processing physical order. Packaging and shipping."

  Scenario: Process Digital Order
    Given a digital order factory
    When I create a digital order
    Then the result should be "Processing digital order. Sending download link."