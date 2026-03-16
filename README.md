# Group 2 -Guleng, Hadjinor, Rico

## Stundent Performance Prediction

One of the commonly used techniques for student performance prediction is the Naive Bayes classifier, a probabilistic algorithm based on Bayes' Theorem. This method calculates the probability that a student will pass or fail based on several independent features. Because of its simplicity, efficiency, and good performance on small datasets, Naive Bayes is widely used in educational research and classification problems.

Predicting student performance helps instructors make better decisions in monitoring student progress. For example, students with poor attendance or low quiz scores may be identified early, allowing teachers to provide guidance or intervention before final examinations. This improves learning outcomes and reduces the number of failing students.

In this study, student performance prediction is done using features such as attendance, study hours, assignment score, and quiz score, and the result is classified into Pass or Fail using the Naive Bayes classification formula. The goal is to demonstrate how probability-based classification can be applied to real educational data to support decision-making in academic environments.

## Features/Factors
| FACTORS | VALUES |
| :--- | :--- |
| Attendance | Good, Average, Poor |
| Study Hours | Long, Short |
| Assignment Score | A, B, C |
| Quiz Score | High, Mid, Low |
| Results | Pass, Fail |

## Datasets
| Student | ATTENDANCE | STUDY HOURS | ASSIGNMENT SCORE | QUIZ SCORE | RESULTS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| S1 | Good | Short | B | Mid | Pass |
| S2 | Good | Long | A | Mid | Pass |
| S3 | Good | Short | B | Mid | Pass |
| S4 | Good | Short | B | Mid | Pass |
| S5 | Good | Long | A | Mid | Pass |
| S6 | Good | Short | B | Mid | Pass |
| S7 | Good | Long | B | Mid | Pass |
| S8 | Good | Short | B | Mid | Pass |
| S9 | Good | Short | B | Mid | Pass |
| S10 | Good | Short | B | Mid | Pass |
| S11 | Good | Long | A | High | Pass |
| S12 | Average | Short | B | Low | Fail |
| S13 | Average | Long | B | Mid | Fail |
| S14 | Good | Short | B | Mid | Pass |
| S15 | Average | Long | B | Mid | Fail |
| S16 | Poor | Short | B | Low | Fail |
| S17 | Poor | Short | C | Mid | Fail |
| S18 | Good | Long | A | Mid | Pass |
| S19 | Good | Short | B | Mid | Pass |
| S20 | Good | Short | B | Mid | Pass |
| S21 | Good | Short | A | High | Pass |
| S22 | Average | Long | A | High | Pass |
| S23 | Poor | Short | B | Mid | Fail |
| S24 | Good | Long | A | High | Pass |
| S25 | Good | Long | B | High | Pass |
| S26 | Average | Short | A | Mid | Pass |
| S27 | Poor | Short | B | Low | Fail |
| S28 | Average | Long | A | High | Pass |
| S29 | Good | Short | A | Mid | Pass |
| S30 | Average | Long | B | Mid | Pass |

## Survey Summary Charts
#### Attendance
![Attendance Chart](data/attendance.png)
#### Study Hours 
![Study Hours Chart](data/stud.png)
#### Assignment Score 
![Assignment Score Chart](data/assign.png)
#### Quiz Score 
![Quiz Score Chart](data/quiz.png)
## Overall Result
![Results Probability](data/res.png)

## How to run the app

#### Clone the Repository
```bash
git clone https://github.com/norjhachie/Group_2-NaiveBayesClassifier-Guleng_Hadjinor_Rico.git
cd Group_2-NaiveBayesClassifier-Guleng_Hadjinor_Rico
```
#### Install Dependencies
```bash
pip install streamlit pandas scikit-learn
```
#### Run the Application (VSCode Terminal)
```bash
python -m streamlit run app.py
```
## How the model works
#### Step 1:
Machine learning models cannot read English words like "Good" or "High." They only understand math.
The OrdinalEncoder acts as a translator. It looks at your CSV and turns the categories into numbers. For example:

Good = 2, Average = 1, Poor = 0

High = 2, Mid = 1, Low = 0

#### Step 2:
Before looking at the student's specific traits, the model looks at your whole CSV file and asks: "Overall, what are the baseline odds of ANY student passing?"
If your CSV has 50 Passes and 50 Fails, the baseline is exactly 50% for Pass and 50% for Fail.

#### Step 3:
Next, the model isolates each individual trait the user selected and checks its history in the CSV:

Clue 1: Out of everyone who Passed in the past, how many had Good Attendance?

Clue 2: Out of everyone who Passed, how many had Long Study Hours?

Clue 3: Out of everyone who Passed, how many had an A?

Clue 4: Out of everyone who Passed, how many had High Quiz Scores?

It then does the exact same calculation for everyone who Failed.

#### Step 4:
The model takes the Baseline probability and multiplies it by the probability of all 4 clues combined.

Pass Score = (Baseline Pass) × (Odds of Good given Pass) × (Odds of Long given Pass) × (Odds of A given Pass) × (Odds of High given Pass)

Fail Score = (Baseline Fail) × (Odds of Good given Fail) × (Odds of Long given Fail) × (Odds of A given Fail) × (Odds of High given Fail)

#### Step 5:
Finally, it compares the total Pass Score against the total Fail Score.
If the Pass Score is higher (e.g., 95% to 5%), it outputs "PREDICTION: The student will PASS."

# Observation
