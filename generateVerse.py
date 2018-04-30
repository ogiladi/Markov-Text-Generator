import TextParser as tp
import MarkovTextGenerator as mtg

def main():
    created_macbeth, created_bible, created_trial, created_karamazov = False, False, False, False

    input = 0
    while input != 5:
        input = int(raw_input("Choose a text to build the sentence:\n 1. Shakespeare's Macbeth\n 2. The Old Testament\n 3. Kafka's The Trial\n 4. Dostoevsky's Brothers Karamazov\n 5. Quit\nEnter your choice:  "))
        if input != 5:
            numWords = int(raw_input("Enter the numbr of words in the sentence: "))
        if input == 1:
            if not created_macbeth:
                created_macbeth = True
                parser_macbeth = tp.TextParser('text_macbeth.txt')
                generator_macbeth = mtg.TextGenerator(parser_macbeth)
            print
            print generator_macbeth.generateSentence(numWords)
            print
        elif input == 2:
            if not created_bible:
                created_bible = True
                parser_bible = tp.TextParser('text_bible.txt')
                generator_bible = mtg.TextGenerator(parser_bible)
            print
            print generator_bible.generateSentence(numWords)
            print
        elif input == 3:
            if not created_trial:
                created_trial = True
                parser_trial = tp.TextParser('text_the_trial.txt')
                generator_trial = mtg.TextGenerator(parser_trial)
            print
            print generator_trial.generateSentence(numWords)
            print
        elif input == 4:
            if not created_karamazov:
                created_karamazov = True
                parser_karamazov = tp.TextParser('text_karamazov.txt')
                generator_karamazov = mtg.TextGenerator(parser_karamazov)
            print
            print generator_bible.generateSentence(numWords)
            print
        elif input == 5:
            break


if __name__ == '__main__':
    main()
