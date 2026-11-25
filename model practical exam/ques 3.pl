% Student facts
student(101, kavin).
student(102, arun).
student(103, priya).

% Course facts
course(c1, python).
course(c2, java).
course(c3, ai).

% Faculty facts
faculty(f1, ravi).
faculty(f2, kumar).

% Enrollment facts
enrolled(101, c1).
enrolled(102, c2).
enrolled(103, c1).
enrolled(101, c3).

% Rule
course_student(Name, Course) :-
    student(ID, Name),
    enrolled(ID, C),
    course(C, Course).