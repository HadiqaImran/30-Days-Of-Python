'''
class Statistics:
    def __init__(self, data):  
        self.A=data.copy()
    def count (self):
        return len(self.A)
    def sum (self):
        total=0
        for i in self.A:
            total+=i
        return total
    def min (self):
        I=sorted(self.A)
        return I[0]
    def max (self):
        I=sorted(self.A)
        return I[-1]
    def range (self):
        I=sorted(self.A)
        return I[-1]-I[0]
    def mean (self):
        return round(self.sum()/self.count())
    def median(self):
        S = sorted(self.A)
        half = int(self.count() / 2)
        if self.count() % 2 == 0:
            return (S[half] + S[half + 1]) / 2
        else:
            return S[half]
    def mode (self):
        j=0
        max_count=0
        saya=self.A[0]
        while j<self.count():
            mia=self.A[j]
            i=j+1
            c=1
            while i<self.count():
                if self.A[i]==mia:
                    c+=1
                i+=1
            if (c>max_count):
                max_count=c
                saya=mia
            j+=1
        return f'mode:{saya},count:{max_count}'
    def var(self):
        m = self.sum() / self.count()
        total = 0
        for i in self.A:
            total += (i - m) ** 2
        return round(total / self.count(), 1)
    

    def std(self):
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        frequency = {}
        for i in self.A:
            frequency[i] = frequency.get(i, 0) + 1
        result = []
        for k, v in frequency.items():
            result.append((round(v / self.count() * 100, 1), k))
        return sorted(result, reverse=True)


age = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=Statistics(age)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
'''
#Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
class PersonAccount():
    def __init__ (self, firstname='A', lastname='l', incomes=[0,0], expenses=[0,0], properties=['0','0']):
        self.FN=firstname
        self.LN=lastname
        self.i=incomes
        self.e=expenses
        self.p=properties
    def account_balance(self):
        return self.total_i() - self.total_e()
    def total_i (self):
        total=0
        for k in self.i:
            total+=k
        return total
    def total_e (self):
        total=0
        for k in self.e:
            total+=k
        return total
    def add_i (self,a):
        self.i.append(a)
    def add_e (self,a):
        self.e.append(a)   
    def account_info(self):
        print("FirstName: ", self.FN)
        print("LastName: ", self.LN)
        print("Incomes: ", self.i)
        print("Expenses: ", self.e)
        print("Properties: ", self.p)


P=PersonAccount("Ali", "Hamza", [13,42,23], [92,28,19,83], ['Villa', 'House'])
P.account_info()
P.add_i(19)
P.account_info()