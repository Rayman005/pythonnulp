import random
    
def func (v):
    sum += i for i in v
    return {'sum': sum, 'avg': sum/len(v)}

def main():
    v = [int(random.random()*100)-50 for i in range(int(random.random()*10)+10)]

    print(v)
    print(func(v)) 

if __name__ == "__main__":
    main()
