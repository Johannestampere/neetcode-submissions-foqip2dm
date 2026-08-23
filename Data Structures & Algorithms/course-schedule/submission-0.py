class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) #prereq->course
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        can_take_queue = deque() # initially all courses with 0 prereqs
        for course in range(numCourses):
            if indegree[course] == 0:
                can_take_queue.append(course)

        courses_taken = 0
        while can_take_queue:
            course = can_take_queue.popleft()
            courses_taken += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    can_take_queue.append(next_course)


        return courses_taken == numCourses