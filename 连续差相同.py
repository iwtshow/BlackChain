


r = [[1,3],[3,0,1],[2],[0]]
def canVisitAllRooms(rooms):
    room_nums = [ i for i in  range(1,len(rooms))]
    keys = list(set(rooms[0]))
    used = []
    while True:
        if len(keys)==0:
            break
        now = keys.pop()
        if now in room_nums:
            room_nums.remove(now)
            used.append(now)
            for term in r[now]:
                if term not in keys:
                    keys.apppend(term)

    if len(room_nums) == 0:
        return True
    else:
        return  False

