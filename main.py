

#TODO 1.how does a flash card app work
#     make a class for a word each word has a status and a difficulty
# in this app u see:
#                       1-user sees a name orderly from the list of the words up to 17 words per session 10 from review section and 7 from new words section
#                       2- in one form user sees the meaning of the word and then user can choose to move to each of provided websites to see the results and then come back
#                       3-user can decide either to :
#                                                       *skip the word by setting an kown tag to the word
#                                                       *manage the word to be shown in the next day by setting medium tag
#                                                       *manage the word to be shown on the next weak  \by setting easy tag
#                                                       *manage the word to be shown on current session again by setting hard tag
# words marked as know should be deleted from the list
from web_frame_page import Web_Frame
import sys
from word import Words
from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow,
    QPushButton, QToolBar)
from word_page import Word_Page
from review_page import Review_Page
def main():
    app = QApplication(sys.argv)
    global word_page,web_frame,current_word,current_meaning,words,review_page

    words=Words()
    word_page=Word_Page()
    web_frame=Web_Frame()
    review_page=Review_Page()

    next_word()
    web_frame.backBtn.clicked.connect(web_back)
    word_page.easy.clicked.connect(lambda: save_word("easy"))
    word_page.medium.clicked.connect(lambda: save_word("medium"))
    word_page.hard.clicked.connect(lambda: save_word("hard"))
    word_page.known.clicked.connect(lambda: save_word("known"))
    review_page.check.clicked.connect(check_review)






    sys.exit(app.exec_())

def set_page(url):
    web_frame.load(url)
    web_frame.show()
def web_back():
    web_frame.hide()
def save_word(difficulty):
    words.fetch_and_replace(difficulty)
    next_word()
#TODO: the main loop of the program check if the word is for learning or for review
#           if its for learning you should extract new words from the list and then show the page word
#           then save the word in the review section
#           if its review then show the review page if the user answers correctly add it to the list of the review by the next priority
#                                                   if the user answer is incorrect then show the user the page word of the word and then renew the priority of the word
def next_word():

    if(not words.is_finished()):
        current_word, current_meaning,mode = words.show_word()
        print(3232)

        if mode=="NEW":
            show_new(current_word, current_meaning)

        elif mode=="REVIEW":
            show_review(current_word, current_meaning)

    else:
        word_page.close()
        review_page.close()
        web_frame.close()
        #finish.show
def show_new(current_word, current_meaning):
    word_page.word.clear()
    word_page.meaning.clear()
    word_page.word.setText(current_word)
    word_page.meaning.setText(current_meaning)
    word_page.update()
    url = "https://www.vocabulary.com/dictionary/" + str(current_word)
    word_page.vocabulary.clicked.connect(lambda: set_page(url))
    google_url = "https://www.google.com/search?tbm=isch&q=" + str(current_word) + " meaning"
    word_page.google_images.clicked.connect(lambda: set_page(google_url))
    word_page.show()

def show_review(current_word, current_meaning):
    review_page.meaning.setText(str(current_meaning))
    review_page.show()
    global review_word
    review_word=current_word
def check_review():
    word=str(review_page.input.text())
    pass


if __name__ == '__main__':
    main()