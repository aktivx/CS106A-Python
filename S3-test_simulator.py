"""
File: test_simulator.py
-----------------------
Write your solution to the Medical Test Simulator
from section 3 here
"""

import random


def simulate_tests(num_people, test_accuracy, infection_rate):
    true_positive = 0
    accurate_positive_test = 0
    false_negative_test = 0
    true_negative = 0
    accurate_negative_test = 0
    false_positive_test = 0
    for i in range(num_people):
        is_positive = random.random() < infection_rate
        if is_positive:
            true_positive += 1
            is_accurate = random.random() < test_accuracy
            if is_accurate:
                accurate_positive_test += 1
            else:
                false_negative_test += 1
        else:
            true_negative += 1
            is_accurate = random.random() < 0.99
            if is_accurate:
                accurate_negative_test += 1
            else:
                false_positive_test += 1

    print('True positives: ' + str(true_positive))
    print('False positives: ' + str(false_positive_test))
    print('False negatives: ' + str(false_negative_test))
    print('true negatives: ' + str(true_negative))

    incorect_positive = false_positive_test / (accurate_positive_test + false_positive_test)
    return incorect_positive

def main():
    num_people = int(input('Number of people: '))
    test_acc = float(input('Test accuracy: '))
    inf_rate = float(input('Infection rate: '))
    print(str(simulate_tests(num_people, test_acc, inf_rate)) + '% of positive tests were incorrect')



if __name__ == "__main__":
    main()
