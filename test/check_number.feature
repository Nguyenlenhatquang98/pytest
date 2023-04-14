Feature: Check number

    @success
    Scenario Outline: I'm learning coding
        Given I have a number <num1>
        When I multiple that with number <num2>
        Then I verify that with number <num3>

        Examples:
        |num1       |num2          |num3        |
        |5          |10            |50          |

    @failed
    Scenario Outline: I'm learning coding failed
        Given I have a number <num1>
        When I multiple that with number <num2>
        Then I verify that with number <num3>

        Examples:
        |num1       |num2          |num3        |
        |6          |10            |50          |