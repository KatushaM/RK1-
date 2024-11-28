import random
def gen_random(num_count, begin, end): 
    return [random.randint(begin, end) for i in range(num_count)]
  
def main():
    print(str(gen_random(12,1,100)).strip('[]'))
    
if __name__ == "main":
    main()
