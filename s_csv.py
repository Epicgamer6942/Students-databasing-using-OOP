import csv
class Files:
    def __init__(self,fName,lst,back_lst = []):
        self.fName = fName
        self.lst = lst
        self.back_lst = back_lst
        
    def add(self,rollback = False):
        if rollback == False:
            with open(self.fName,"a",newline = "") as f1:
                writerObj = csv.writer(f1,delimiter="|")
                writerObj.writerow(self.lst)
        else:
            with open(self.fName,"a",newline = "") as f1:
                writerObj = csv.writer(f1,delimiter="|")
                writerObj.writerows(self.back_lst)
   
    def read(self):
        with open(self.fName,"r",newline = "") as f1:
            readerObj = csv.reader(f1,delimiter = "|")
            l1 = list(readerObj)
            return l1
    
    def delrec(self,name):
        with open(self.fName,"r",newline = "") as f1:
            readerObj = csv.reader(f1,delimiter = "|")
            l1 = list(readerObj)
            l2 = []
            for i in range(len(l1)):
                if name in l1[i]:
                    with open("rollback.csv","w",newline = "") as f2:
                        writerObj = csv.writer(f2, delimiter="|")
                        writerObj.writerow(l1[i])
                    self.back_lst.append(l1[i])
                elif name not in l1[i]:
                    l2.append(l1[i])
                    print("This name is not present please try again 😊")
            f1.close()
        with open(self.fName,"w",newline = "") as f3:
            writerObj = csv.writer(f3, delimiter="|")
            writerObj.writerows(l2)


   
    def rollback(self):
        print("Change will be rolledback")
        
        Files.add(self,rollback = True)
       
   
    def commit(self):
        ANS = "AGREE"
        inp = input("These changes are irrevertible type \'AGREE\' to confirm: ")
        if inp == ANS:
            with open("rollback.csv","w",newline = "") as f2:
                print("Changes have been successfully commited")
        else:
            print("Changes arent commited yet, if you didnt want to make these changes,\nUse the \'rollback\' method")
            



            
            

                    



            
        