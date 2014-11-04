from random import randrange
if __name__ == '__main__':
    print("INTEGER DIVISIONS")
        
    max_number = 5              
    number_of_questions = 10    
    
    for question_number in range(1, number_of_questions + 1):
        
        divisor = randrange(1, max_number)

        
        quotient = randrange(max_number)
        
        
        dividend = divisor * quotient
        
        
        answer_string = input(str(dividend) + " / " + str(divisor) + " = ").strip()
        
        try:
            
            answer_int = int(answer_string)

            if answer_int == quotient:
                            
                print("CORRECT!")
            else:
                        
                print("INCORRECT!")
        except ValueError:
            
            print("Please enter Integers only!")
