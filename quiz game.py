print ("Heyy! Welcome to the Game ")
playing=input("Do you want to play the game? ")
if playing !="yes":
    quit( )
print("Okay! Let's Begin ")
score = 0

answer=input("Rachel got a job with which company in Paris?   ")
if answer.lower() == "louis vuitton":
       print("Woahooo :) ")
       score+=1
else:
    print(" Oops:( ")
    
answer=input("What is Chandler Bing's middle name?   ")
if answer.lower() == "muriel":
    print("Correct :)")
    score +=1
else:
  print("Oops :( ")
  
  
answer=input("What was the occupation of Rachel's fiancé Barry Farber?   ")
if answer.lower() =="orthodontist":
                     print("Woahoo :)")
                     score +=1
else:
   print("Oops :( ")
    
answer=input("Who was the maid of honor at Monica's wedding? ")
if answer.lower() =="rachel":
    print ("Woahoo :)")
    score +=1
else:
    print("Oops :( ")
    
answer=input("What store does Phoebe hate?   ")
if answer.lower() =="pottery barn":
        print("Woahoo :) ")
        score +=1
else:
        print("Oops :( ")
        
        answer=input("How many seasons of Friends are there?   ")
if answer.lower() == "ten":
            print("Woahoo :)" )
            score +=1
else:
            print("Oops :( ")
            
answer=input("How many times did Ross get divorced?   ")
if answer.lower() =="three":
                print("Woahoo :) ")
                score +=1
else:
                print("Oops :( ")
answer=input("What are the names of Ross and Monica's parents?   ")
if answer.lower() =="jack and judy geller":
 
                    print("Woahoo :) ")
                    score +=1
else:
                    print("Oops:( ")
                     
answer=input("Which Sprouse brother played Ross' son Ben?   ")
if answer.lower() == "cole":
                        print("Woahoo :( ")
                        score +=1
else:
 print("Oops :( ")
                        
answer=input("Monica dated an ophthalmologist named?   ")
if answer.lower() =="richard":
                            print("Woahoo :) ")
                            score+=1
else:
                            print("Oops :( ")
                            
                            
                            
                            
print("You got"    +  str  (score)   + "  questions correct  ")
print("You scored"  + str  (  score/ 10* 100) + " %  ")





print("I hope you enjoyed! Thankyou for playing:) ")
                        
            
            
                
