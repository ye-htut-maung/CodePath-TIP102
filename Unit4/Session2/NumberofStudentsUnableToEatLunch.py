from collections import deque

def munchTime(sandwiches, students):
    sandwiches_stack = deque()
    students_queue = deque()

    for i in range(0, len(sandwiches)) :
        sandwiches_stack.append(sandwiches[i])
        students_queue.append(students[i])

    counter = 0
    while(len(students_queue) != 0 and len(students_queue) > counter):

        student =  students_queue.popleft()
        sandwich = sandwiches_stack.popleft()

        if student != sandwich:
            students_queue.append(student)
            sandwiches_stack.appendleft(sandwich)
            counter += 1
        else:
            counter = 0
        
    return len(students_queue)
    






# students = [1,1,1,0,0,1]
# sandwiches = [1,0,0,0,1,1]
# students = [1]
# sandwiches = [0]
students = [1,1,0,0]
sandwiches = [0,1,0,1]
#Output: 3
# print("Students unable to eat: " + str(munchTime(sandwiches, students)))
print(munchTime(sandwiches, students))
