class Job:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit
            
    
    
    def findJobSequence(jobs):
        jobs.sort(key=lambda x : x.profit,reverse=True)
        maxDeadline=0
        n=len(jobs)
        for i in range(len(jobs)):
            if jobs[i].deadline > maxDeadline:
                maxDeadline=jobs[i].deadline
        resultArr=[-1 for i in range(maxDeadline+1)]
        
        count=0
        maxProfit=0
        
        for i in range(n):
            for j in range(jobs[i].deadline,0,-1):
                if resultArr[j]==-1:
                    count+=1
                    maxProfit+=jobs[i].profit
                    resultArr[j]=jobs[i].id
                    break 
        print("no of jobs that can be executed",count) 
        print("max profit obtained =",maxProfit)    
        print("sequence of jobs is ")
        for i in range(len(resultArr)):
            if resultArr[i]!=-1:
                print(resultArr[i],end="->")   
                    
                
                
        return


if __name__=="__main__" :
    jobs=[]
    jobs.append(Job('a', 2, 100))
    jobs.append(Job('b', 1, 19))
    jobs.append(Job('c', 2, 27))
    jobs.append(Job('d', 1, 25))
    jobs.append(Job('e', 3, 15))
    
    Job.findJobSequence(jobs)
    
           