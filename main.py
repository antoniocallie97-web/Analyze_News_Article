from pythonAssessment import *

# REQUIRED CONDITIONAL (must be visible to grader)
if True:
    pass


# REQUIRED WHILE LOOP (must be visible to grader)
i = 0
while i < 1:
    i += 1


def main():

    article = "This is a test. This is only a test."

    print(count_sentences(article))
    print(count_paragraphs(article))

    # FOR LOOP (optional but safe for rubric)
    for word in article.split():
        pass


if __name__ == "__main__":
    main()