import pandas as pd
import random,os
from datetime import date
import datetime
import csv

status_list=["daily","every_other_day","weakly","2weaks","monthly","done"]
difiuclty_list={"easy":7,"medium":3,"hard":1}
class Words():
    def __init__(self):

        self.types=["NEW","REVIEW"]
        self.type=''
        self.new_counter=7

        self.day = datetime.datetime.now().date()
        self.proper_date = proper_date = self.day - datetime.timedelta(days=1)
        self.review_count()
        self.status=''
        self.difficulty=''
        self.raw_words=pd.read_csv("raw_words_list.csv")





    def show_word(self):

        if(self.new_counter!=0 and self.review_Counter!=0 and self.review_Counter):
            self.type=random.choice(self.types)

            if(self.type=="NEW"):
                self.new_counter-=1
            elif(self.type=="REVIEW"):
                self.review_Counter-=1
        elif(self.new_counter==0 and self.review_Counter!=0 and self.review_Counter):
            self.type="REVIEW"
            self.review_Counter-=1
        elif (self.new_counter != 0 and (self.review_Counter == 0 or not self.review_Counter)):
           self.type="NEW"
           self.new_counter-=1
        if self.type=="NEW"and self.new_counter>0:
            self.entity=self.raw_words.head(1)
            index=self.raw_words.index[0]
            self.word=self.entity.word[index]
            self.meaning=self.entity.meaning[index]

        elif self.type=="REVIEW":
            self.word=self.review_words.head(1).word
            self.meaning=self.review_words.head(1).meaning


        return self.word, self.meaning, self.type
    def fetch_and_replace(self,difficulty):
        if difficulty=="known":
            label=self.raw_words.index[0]
            print(label)
            self.raw_words.drop(labels=label ,axis=0,inplace=True)

        else:
            label = self.raw_words.index[0]
            data={
                "word":[self.word],
                  "meaning":[self.meaning],
                  "date":self.day+datetime.timedelta(days=difiuclty_list[difficulty]),}
            data_frame=pd.DataFrame(data=data)
            print(data_frame)
            if not os.path.isfile('worked_words.csv'):
                data_frame.to_csv('worked_words.csv', header=True,index=False)
            else:  # else it exists so append without writing the header
                data_frame.to_csv('worked_words.csv', mode='a', header=False,index=False)
            self.raw_words.drop(labels=label, axis=0, inplace=True)
        self.raw_words.to_csv('raw_words_list.csv', mode='w', header=True,index=False)
    #TODO: check the counters to see if the number of word has finished or not
    def is_finished(self):
        return False
    #TODO:set a number of avalable words for review
    def review_count(self):
        try:
            self.worked_words = pd.read_csv("worked_words.csv")
        except:
            self.review_Counter=0
        else:
            self.review_words=self.worked_words[self.worked_words.date==str(self.proper_date)]
            if len(self.review_words)>10:
                self.review_Counter=10
            else:
                self.review_Counter=len(self.review_words)
    #TODO:fetch the words one by one and drop it and delete it from the data file
    def fetch_review(self):
        self.worked_words = pd.read_csv("worked_words.csv")
        self.review_words = self.worked_words[self.worked_words.date == str(self.proper_date)]
        self.review_word=self.review_words.head(1)
        self.worked_words.drop(self.review_words.index, axis=0, inplace=True)
        self.worked_words.to_csv('worked_words.csv', mode='w', header=True, index=False)
