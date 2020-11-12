# https://leetcode.com/problems/keys-and-rooms
# Leetcode #841

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        
        n_rooms = len(rooms)
        
        def backtrack(room):
            if room in visited:
                return
            
            visited.add(room)
            
            for key in rooms[room]:
                backtrack(key)
                
        backtrack(0)
        
        if len(visited)==n_rooms:
            return True

        else: 
            return False