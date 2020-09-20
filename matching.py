import numpy as np 
import random as random
import scipy as spatial 
import spacy

nlp = spacy.load("en_core_web_sm")  

#high school 5%
#university 20%
#major 20%
#native country 5%
#language 20%
#availability (in terms of standard time zone) 20%
#personality 5%
#services 5%
#data intialization
weight_vec = [5, 20, 20, 5, 20, 20, 5, 5]
data_matrix = np.array([["Fraser_Heights_Secondary", "North_Surrey_Secondary", "Semiahmoo_Secondary", "Pacific_Academy", "Earl_Haig", "Colonel_Bay", "Newburry_Park", "Saint_Georges"],
              ["MIT", "Stanford", "Harvard", "Princeton", "Caltech", "Upenn", "Cornell", "UofToronto", "UofWaterloo", "UofTokyo", "Tsinghua", "Peking", "Cambridge", "Oxford"],
              ["Computer_Science", "Electricial_Engineering", "Software_Engineering", "Computer_Engineering", "Politics", "Biology", "Chemistry", "Pre-Med", "Statistics", "Psychology", "Business", "Econ"],
              ["USA", "India", "Canada", "China", "Korea", "Japan", "Germany", "Russia", "Brazil", "France", "Spain", "UK", "Italy", "Norway", "Jamaica"],
              ["English", "Mandarin", "Cantonese", "Korean", "Japanese", "German", "Russian", "French", "Spanish", "Italian"],  
              ["Early_Morning", "Morning", "Afternoon", "Late_Afternoon", "Evening", "Night", "Midnight"],
              ["ENFJ", "INFJ", "INTJ", "ENTJ", "ENFP", "INFP", "INTP", "ENTP", "ESFP", "ISFP", "ISTP", "ESTP", "ESFJ", "ISFJ", "ISTJ", "ESTJ"],
              ["Mentoring", "Tutoring", "Counselling"]])


data_matrix = '\n'.join(' '.join('%s' %x for x in y) for y in data_matrix)+'\n'
print(data_matrix)
text_file = open("data_matrix.txt", "w")
text_file.write("%s" % data_matrix)
text_file.close()

#mentor mentee random generation
mentors, mentees = [], []
with open("data_matrix.txt") as f:
       for line in f:
              mentor_list, mentee_list = [],[]
              e = line.strip().split(' ')
              for i in range(10):
                     mentor_list.append(random.choice(e))
                     mentee_list.append(random.choice(e))
              mentors.append(mentor_list)
              mentees.append(mentee_list)
mentors = np.array(mentors).T
mentees = np.array(mentees).T
mentors = '\n'.join(' '.join('%s' %x for x in y) for y in mentors)+'\n'
mentees = '\n'.join(' '.join('%s' %x for x in y) for y in mentees)+'\n'

print(mentors)
print(mentees)
text_file = open("mentors.txt", "w")
text_file.write("%s" % mentors)
text_file.close()
text_file = open("mentees.txt", "w")
text_file.write("%s" % mentees)
text_file.close()

compatibility_matrix = np.zeros((10,10))
with open("mentees.txt", "r") as f1, open("mentors.txt", "r") as f2:
       l1 = f1.readlines()
       l2 = f2.readlines()
       for idx1, line1 in enumerate(l1):
              e1 = line1.strip().split(' ')
              for idx2, line2 in enumerate(l2):
                     e2 = line2.strip().split(' ')
                     raw_vec = []
                     for i in range(8):
                            token1 = nlp(str(e1[i]))
                            token2 = nlp(str(e2[i]))
                            raw_vec.append(float(token1.similarity(token2)))
                     compatibility_matrix[idx1][idx2] = np.dot(weight_vec, raw_vec)

compatibility_matrix = '\n'.join(' '.join('%s' %x for x in y) for y in compatibility_matrix)+'\n'
print(compatibility_matrix)  
text_file = open("compatibility_matrix.txt", "w")
text_file.write("%s" % compatibility_matrix)
text_file.close()  
