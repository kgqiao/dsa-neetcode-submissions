class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # prereq[i][0] = course
        # prereq[i][1] = prereq course

        indeg = [0] * numCourses # Initalize empty arr to hold number of prereqs this class has remaining
        out = []
        adj = defaultdict(list) #Make an empty hashtable (defaultdict(list)): defaultdict(list) just saves you from having to pre-populate the keys

        for course, prereq in prerequisites: #add the prereq tags to the courses
            adj[prereq].append(course) # Add for each prereq which courses are tied to it
            indeg[course] += 1 #increment # of prereqs this class has by 1
    
        # queue thru all those w/ indeg == 0 # those that can already be taken bc have no prereqs
        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        while q: # While queu is not empty, go through all until indeg for all courses are empty
            cur = q.popleft() # pop out currently can be taken course
            out.append(cur) #can be added to course list

            for post in adj[cur]: #if cur course is a prereqt of any values, can take them off
                indeg[post] -= 1

                if indeg[post] == 0: # if post course no longer has nay more courses, can add to course list
                    q.append(post)
        
        if len(out) != numCourses: #if numCourses don't match, then wrong, else return list
            return []
        else: 
            return out