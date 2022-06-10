#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
def merge(p1,p2):
    if p1 == None: return p2
    if p2 == None: return p1
    
    dummy = Node(-1)
    tail = dummy
    
    while p1 and p2:
        if p1.data <= p2.data:
            tail.bottom = p1
            p1 = p1.bottom
        else:
            tail.bottom = p2
            p2 = p2.bottom
        
        tail = tail.bottom
        tail.bottom = None
    
    if p1:
        tail.bottom = p1
    
    if p2:
        tail.bottom = p2
    
    return dummy.bottom
            

def flatten(root):
    #Your code here
    dummy = Node(-1)

    p2 = root
    while p2:
        p1 = dummy.bottom
        
        temp = p2.next
        p2.next = None
        
        dummy.bottom = merge(p1,p2)
        p2 = temp
        
    return dummy.bottom
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends