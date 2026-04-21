# Grader class for Data C140 HW12.

import hashlib
import numpy as np

class Autograder():
    def hash_student_answer(self, student_ans):
        student_ans_str = str(student_ans)
        student_ans_bytestring = student_ans_str.encode('utf-8')

        student_ans_hash = hashlib.sha256(student_ans_bytestring).hexdigest()

        return student_ans_hash
    
    def grade_q2a(self, student_ans):
        correct_ans_hash = 'd2cbad71ff333de67d07ec676e352ab7f38248eb69c942950157220607c55e84'

        student_ans_hash = self.hash_student_answer(student_ans)

        if student_ans_hash == correct_ans_hash:
            print("CORRECT")
        else:
            raise ValueError("QUESTION 2A INCORRECT")

    def grade_q2b(self, student_ans):
        # 5 decimal places

        correct_ans_hash = '63bb4beb3ba65ffd0812a9c96f60127133b0af3dea0d4d4fa2585c7356f220b5'

        student_ans_hash = self.hash_student_answer(student_ans)
        
        if student_ans_hash == correct_ans_hash:
            print("CORRECT")
        else:
            raise ValueError("QUESTION 2B INCORRECT")
        