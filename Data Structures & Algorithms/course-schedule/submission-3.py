class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        completed = 0

        while queue:

            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                indegrees[next_course] -= 1

                if indegrees[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses

            

        

