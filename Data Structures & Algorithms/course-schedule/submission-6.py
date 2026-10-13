class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        queue = deque()
        completed = 0

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                completed += 1

        while queue:

            prereq = queue.popleft()

            for course in graph[prereq]:
                indegrees[course] -= 1

                if indegrees[course] == 0:
                    queue.append(course)
                    completed += 1

        return completed == numCourses


            

        

