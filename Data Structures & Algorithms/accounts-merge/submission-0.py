class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
         
        # keep an email -> name map and an email -> [all neighbor emails] graph
        # emails under every connected component are one account's


        # create the email->name map and the graph

        email_to_name = {}
        graph = defaultdict(list)

        for acc in accounts:

            name = acc[0]
            first_email = acc[1]

            email_to_name[first_email] = name

            for email in acc[1:]:
                email_to_name[email] = name
                graph[email].append(first_email)
                graph[first_email].append(email)

        # BFS

        res = []
        visited = set()

        for email in email_to_name:

            if email in visited:
                continue
            
            stack = [email]
            visited.add(email)
            emails = []

            while stack:
                cur = stack.pop()
                emails.append(cur)

                for neighbour_email in graph[cur]:
                    if neighbour_email not in visited:
                        stack.append(neighbour_email)
                        visited.add(neighbour_email)
            
            res.append([
                email_to_name[email],
                *sorted(emails)
            ])

        return res



        
