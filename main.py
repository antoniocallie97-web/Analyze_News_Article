from pythonAssessment import count_specific_word


def main():
    # Sample test article (you can also load from file if you want)
    article = """
    ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation.

    ACME Inc. has launched a groundbreaking device called the Apple Pie Master.
    It uses AI to automate pie making and ensure perfect results every time.

    The Apple Pie Master can peel apples, mix ingredients, and bake pies efficiently.
    Apple pie lovers are excited about this innovation.
    """

    print("=== TEST CASES ===")

    # Test 1
    print(count_specific_word(article, "apple"))

    # Test 2
    print(count_specific_word("apple apple banana banana banana", "banana"))

    # Test 3
    print(count_specific_word("", "test"))


if __name__ == "__main__":
    main()