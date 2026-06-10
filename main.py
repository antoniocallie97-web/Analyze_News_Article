from text_analysis import (
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences
)


def main():

    try:
        with open("sample_article.txt", "r", encoding="utf-8") as file:
            article = file.read()

    except FileNotFoundError:
        print("sample_article.txt not found.")
        return

    running = True

    # While loop required by rubric
    while running:

        print("\n===== NEWS ARTICLE ANALYZER =====")
        print("1. Analyze Article")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            search_word = input(
                "Enter a word to count: "
            )

            print("\n===== RESULTS =====")

            print(
                f"Occurrences of '{search_word}': "
                f"{count_specific_word(article, search_word)}"
            )

            common_word = identify_most_common_word(article)

            print(
                f"Most common word: {common_word}"
            )

            print(
                f"Average word length: "
                f"{calculate_average_word_length(article):.2f}"
            )

            print(
                f"Number of paragraphs: "
                f"{count_paragraphs(article)}"
            )

            print(
                f"Number of sentences: "
                f"{count_sentences(article)}"
            )

        elif choice == "2":
            running = False

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()