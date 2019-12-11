import random

class Lab1:
    
    def func (v):
        sum = 0
        for i in v:
            sum += i
        return {'sum': sum, 'avg': sum/len(v)}

def main():
    v = [int(random.random()*100)-50 for i in range(int(random.random()*10)+10)]

    print(v)
    print(Lab1.func(v)) 

if __name__ == "__main__":
    main()