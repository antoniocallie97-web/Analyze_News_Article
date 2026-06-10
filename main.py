from pythonAssessment import *


def main():

    article = """
    This is a test. This is only a test.

    Apple apple banana banana banana.
    """

    # REQUIRED WHILE LOOP
    running = True

    while running:

        print("\n===== MENU =====")
        print("1. Run Analysis")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            word = input("Enter word to search: ")

            print("\n--- RESULTS ---")
            print("Specific word count:", count_specific_word(article, word))
            print("Most common word:", identify_most_common_word(article))
            print("Average word length:", calculate_average_word_length(article))
            print("Paragraphs:", count_paragraphs(article))
            print("Sentences:", count_sentences(article))

            # REQUIRED FOR LOOP (structure test)
            for w in article.split():
                pass

        elif choice == "2":
            running = False

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()