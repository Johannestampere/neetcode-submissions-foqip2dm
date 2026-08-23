class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites - list of [a, b], must take b before a
        # numCourses - number of courses student must take
        
        # 1) Create a map of prerequisite -> list of courses
        # 2) Create an array to track how many
        # prerequisites are still untaken at the moment
        #   arr[i] - # of prereqs needed to take
        course_map = defaultdict(list)
        untaken = [0] * numCourses
        for cou, pre in prerequisites:
            course_map[pre].append(cou)
            untaken[cou] += 1

        # 3) Create a queue of courses we can complete atm
        can_take = deque()
        num_taken = 0
        # 4) Add every course with 0 prereqs as the courses
        # we can initially take
        for i in range(len(untaken)):
            if untaken[i] == 0:
                can_take.append(i)

        # 5) Do BFS on courses
        while can_take:
            cur = can_take.popleft()
            num_taken += 1
            for next_course in course_map[cur]:
                untaken[next_course] -= 1
                if untaken[next_course] == 0:
                    can_take.append(next_course)
        
        return num_taken == numCourses


