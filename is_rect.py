

# def validSquare(p1, p2, p3, p4):
#     nums = {}
#     p1_to_p2 = pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2)
#     p1_to_p3 = pow(p1[0]-p3[0],2)+pow(p1[1]-p3[1],2)
#     p1_to_p4 = pow(p1[0]-p4[0],2)+pow(p1[1]-p4[1],2)
#     l = [p1_to_p2,p1_to_p3,p1_to_p4]
#     l.sort()
#     print(l)
#     if  l[-1] != l[0]+l[1] or l[0] != l[1]:
#         return  False
#     nums[p1_to_p2] = "p1_to_p2"
#     nums[p1_to_p3] = "p1_to_p3"
#     nums[p1_to_p4] = "p1_to_p4"
#     first = str(nums[l[0]]).split("_")
#     sceond = str(nums[l[1]]).split("_")
#     m1 = eval(first[0])
#     m2 = eval(first[-1])
#     f = (m1[0]-m2[0],m1[1]-m2[1])
#     n1 = eval(sceond[0])
#     n2 = eval(sceond[-1])
#     s = (n1[0]-n2[0],n1[1]-n2[1])
#     if  f[0] * s[0] - f[1] * s[1] == 0:
#         return True
# p1,p2,p3,p4 = [0,0],[1,1],[0,1],[1,0]
# is_valid=validSquare(p1,p2,p3,p4)

def validSquare(p1, p2, p3, p4):
    if p1 == p2 == p3 == p4:
        return False
    p1_to_p2 = (p2[0]-p1[0],p2[1]-p1[1])
    p1_to_p3 = (p3[0]-p1[0],p3[1]-p1[1])
    p1_to_p4 = (p4[0]-p1[0],p4[1]-p1[1])
    lenth12 = pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2)
    lenth13 = pow(p1[0]-p3[0],2)+pow(p1[1]-p3[1],2)
    lenth14 = pow(p1[0]-p4[0],2)+pow(p1[1]-p4[1],2)

    if p1_to_p2[0] * p1_to_p3[0] + p1_to_p2[1] * p1_to_p3[1] == 0:
        if lenth12 + lenth13 == lenth14 and lenth12 == lenth13 :
            label = (p1_to_p2[0]+p1_to_p3[0],p1_to_p2[1]+p1_to_p3[1])
            if label == p1_to_p4:
                return True

    elif p1_to_p2[0] * p1_to_p4[0] + p1_to_p2[1] * p1_to_p4[1] == 0:
        if lenth12 + lenth14 == lenth13 and lenth12 == lenth14:
            label = (p1_to_p2[0]+p1_to_p4[0],p1_to_p2[1]+p1_to_p4[1])
            if label == p1_to_p3:
                return True
    elif p1_to_p3[0] * p1_to_p4[0] + p1_to_p3[1] * p1_to_p4[1] == 0:
        if lenth13 + lenth14 == lenth12 and lenth13 == lenth14:
            label = (p1_to_p3[0]+p1_to_p4[0],p1_to_p3[1]+p1_to_p4[1])
            if label == p1_to_p2:
                return True
    else:
        return False
p1,p2,p3,p4 = [1,1],[0,1],[1,2],[0,0]
is_valid=validSquare(p1,p2,p3,p4)
print(is_valid)



