#==== Algorithm 2017 -- Hw3 ====
#==== Collaborator : B03901134 袁培傑 ====


if __name__ == '__main__':

    n, p = (int(x) for x in input().split(' '))

    semList = [int(input().split(' ')[1]) for _ in range(n)]

    in_degree = [0]*n # how many prerequisite should be taken
    adjList = [[] for _ in range(n)]

    for i in range(p):
        course, prerequisite = (int(x) for x in input().split(' '))
        adjList[prerequisite].append(course)
        in_degree[course] += 1

    # record which courses to be taken at first and second semester
    semesters = [[],[]]
    # if no prerequisites, just take the courses at the semester when they are taught
    for course, number in enumerate(in_degree):
        if number == 0:
            if semList[course] == 2:
                semesters[0].append(course)
            else:
                semesters[semList[course]].append(course)
    left = n
    semCur = 0
    semNext = 1
    coursesCur = []      # courses to be taken at this semester
    coursesNextYear = [] # courses to be taken at next year
    ans = []
    while(True):
        while (len(semesters[semCur])):
            course = semesters[semCur].pop(0)
            left = left - 1
            coursesCur.append(course)
            for adj in adjList[course]:
                in_degree[adj] = in_degree[adj] - 1
                if in_degree[adj] == 0:
                    if semList[adj] == semCur:
                        coursesNextYear.append(adj)
                    else:
                        semesters[semNext].append(adj)

        if(len(coursesCur) == 0):
            if len(ans):
                if ans[-1] == [-1]:
                    raise SystemExit('-1')
            ans.append([-1])
        else:
            coursesCur.sort()
            ans.append(coursesCur)
            if left == 0:
                break
        # refresh
        coursesCur = []
        semesters[semCur] = coursesNextYear
        coursesNextYear = []
        tmp = semCur
        semCur = semNext
        semNext = tmp

    # System Output
    print('%2.1f' % (0.5*len(ans)))
    for courses in ans:
        print(*courses, sep=' ')
