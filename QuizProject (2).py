print('--------------Hello and welcome to QUIZ MANIA--------------')
print('\n\n-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('\nQuiz rules are simple:')
print('--> You will be asked 10 questions based on the topic you choose.')
print('--> You will have 2 attempts per question.')
print('--> Correct answer = +4 points.')
print('--> Incorrect answer (if the final answer is incorrect) = -1 point.')
print('\n****************** ALL THE BEST ******************')
print('\nPlease select any one topic of the following for the quiz:')
print(' 1. Cars')
print(' 2. Hollywood')
print(' 3. Bollywood')
print(' 4. General Knowledge')
score = 0
while True:
    choice =int(input('Make ur choice (enter 1,2,3 or 4): '))
  
    if choice == 1:
        print("\n\n\t\tWelcome to Cars Quiz:-")
        question1 = "\n1)Which is the fastest car in the world?"
        options1 = "  a. Koenigsegg Agrea R\n  b. Bugatti Chiron Super Sport\n  c. Hennessey Venom\n  d. SSC Tuatara\n"
        print(question1)
        print(options1)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")

                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")

                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question2 = "\n2)Which is the most powerful production car in the world?"
        options2 = "  a. Nilo EP9 \n  b. Dodge Demon\n  c. Bugatti Chiron\n  d. Mclaren P1\n"
        print(question2)
        print(options2)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question3 = "\n3)Which automaker has made the most number of cars?"
        options3 = "  a. BMW R\n  b. Suzuki\n  c. Toyota\n  d. Ford\n"
        print(question3)
        print(options3)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question4 = "\n4)Which is the best selling car in the world?"
        options4 = "  a. Toyota Corolla \n  b. Audi A3\n  c. VW Bettle\n  d. Ford Model T\n"
        print(question4)
        print(options4)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
        
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question5 = "\n5)Which automaker takes the longest to make a single car?"
        options5 = "  a. Koenigsegg \n  b. Ferrari\n  c. Lamborghini\n  d. Rolls Royce\n"
        print(question5)
        print(options5)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question6 = "\n6)Which are the longest surviving cars of all time?"
        options6 = "  a. Chevrolet SUBURBAN \n  b. Ford F-Series\n  c. Chevrolet Corvette\n  d. Mercedes SL\n"
        print(question6)
        print(options6)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question7 = "\n7)What is the current Land Speed Record?"
        options7 = "  a. 760km/h \n  b. 1220km/h\n  c. 1580km/h\n  d. 1045km/h\n"
        print(question7)
        print(options7)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "b":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "b":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: b")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question8 = "\n8)Which is the cheapest car ever?"
        options8 = "  a. Tata Nano \n  b. Alto 800\n  c. Mini Cooper\n  d. Mahindra eV\n"
        print(question8)
        print(options8)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question9 = "\n9)When were electric cars produced for the 1st time?"
        options9 = "  a. 1987 \n  b. 2008\n  c. 1905\n  d. 1968\n"
        print(question9)
        print(options9)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question10 = "\n10)Which is the stolen car in the world?"
        options10 = "  a. Honda accord \n  b. Maruti omni\n  c. Hyundai elentra\n  d. Ford Pickup\n"
        print(question10)
        print(options10)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        print("\nYour Final score is "+str(score)+"/40")
        while True:
            if score == 40:
                print("Outstanding!!")
                break
            elif 31 <= score <= 39:
                print("Excellent!!")
                break
            elif 21 <= score <= 30:
                print("Good Work!!")
                break
            elif 11 <= score <= 20:
                print("Can do better!!")
                break
            else:
                print("Increase your knowledge :(")
                break
        break
    elif choice == 2:
        print("\n\n\t\tWelcome to Hollywood Quiz:-")
        question1 = "\n1)What was the name of Lord Voldemort's loyal snake?"
        options1 = "  a. Nagini\n  b. Scabbers\n  c. Basilisk\n  d. Fawkes\n"
        print(question1)
        print(options1)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")

                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")

                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question2 = "\n2)Which movie was incorrectly announced as the winner of Best Picture at the 2017 Academy Awards, during the greatest Oscars flub of all time?"
        options2 = "  a. Moonlight\n  b. Manchester By The Sea\n  c. Hell or High Water\n  d. La La Land\n"
        print(question2)
        print(options2)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question3 = "\n3)Who does Hermione Granger become when she takes a Polyjuice Potion to break into Gringotts Bank?"
        options3 = "  a. Madame Maxime \n  b. Dolores Umbridge \n  c. Bellatrix Lestrange \n  d. Narcissa Malfoy\n"
        print(question3)
        print(options3)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question4 = "\n4)Who was the last holder of the Space Stone before Thanos claims it for his Infinity Gauntlet?"
        options4 = "  a. Thor\n  b. Loki\n  c. The Collector\n  d. Tony Stark\n"
        print(question4)
        print(options4)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
        
            if response == "b":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "b":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: b")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question5 = "\n5)What landmark does Peter Parker rescue his classmates from in Spider-Man: Homecoming?"
        options5 = "  a. Washington Monument\n  b. Statue of Liberty\n  c. Mount Rushmore\n  d. Golden Gate Bridge\n"
        print(question5)
        print(options5)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question6 = "\n6)Which character is played by Winona Ryder in 'Stranger Things'?"
        options6 = "  a. Karen Wheeler\n  b. Terry Ives\n  c. Joyce Byers\n  d. Barbara\n"
        print(question6)
        print(options6)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question7 = "\n7)What is the name of Yoda’s home?"
        options7 = "  a. Grand Moff Tarkin\n  b. Boba Fett\n  c. Snoke\n  d. Count Dooku\n"
        print(question7)
        print(options7)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question8 = "\n8)In what 1979 James Bond movie does the famous spy go to outer space?"
        options8 = "  a. Moonraker\n  b. Spectre\n  c. License to Kill\n  d. Live and Let Die\n"
        print(question8)
        print(options8)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question9 = "\n9)Which film won Academy Award for Best Picture, Palme d'Or, more in 2020?"
        options9 = "  a. Joker\n  b. Parasite\n  c. Ford vs Ferrari\n  d. Little Women\n"
        print(question9)
        print(options9)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "b":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "b":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: b")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question10 = "\n10)Which is the most grossing film of all time?"
        options10 = "  a. Titanic \n  b. Interstellar\n  c. Avatar\n  d. Avengers:End Game\n"
        print(question10)
        print(options10)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        print("\nYour Final score is "+str(score)+"/40")
        while True:
            if score == 40:
                print("Outstanding!!")
                break
            elif 31 <= score <= 39:
                print("Excellent!!")
                break
            elif 21 <= score <= 30:
                print("Good Work!!")
                break
            elif 11 <= score <= 20:
                print("Can do better!!")
                break
            else:
                print("Increase your knowledge :(")
                break
        break
    elif choice == 3:
        print("\n\n\t\tWelcome to Bollywood Quiz:-")
        question1 = "\n1)In 3 Idiots, what is Rancho's real name?"
        options1 = "  a. Ranchoddas Shamaldas Chanchad\n  b. Chatur Ramalingan\n  c. Phunsuk Wangdu\n  d. Viru Sahastrabuddhe\n"
        print(question1)
        print(options1)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")

                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")

                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question2 = "\n2)Who played the female lead in the movie 'Chandni Chowk to China'?"
        options2 = "  a. Rani Mukherjee\n  b. Kajol\n  c. Kareena Kapoor\n  d. Deepika Padukone\n"
        print(question2)
        print(options2)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question3 = "\n3)Who is the director of the movie Paa?"
        options3 = "  a. R. Balki\n  b. Anurag kashyap\n  c. Rajkumar Hirani\n  d. Karan Johar\n"
        print(question3)
        print(options3)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question4 = "\n4)In which year did Amitabh Bachchan debut in Hindi cinema?"
        options4 = "  a. 1960\n  b. 1965\n  c. 1968\n  d. 1969\n"
        print(question4)
        print(options4)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
        
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question5 = "\n5)Which was the first Hindi Movie to receive the national award?"
        options5 = "  a. Kabuliwala\n  b. Do Aankhen Barah Haath\n  c. Mirza Ghalib\n  d. Anuradha\n"
        print(question5)
        print(options5)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question6 = "\n6)The Versatile Bollywood actor Irrfan Khan, who recently passed away, had won National award for which movie?"
        options6 = "  a. Lunch Box\n  b. Paan Singh Tomar\n  c. Life of Pi\n  d. Haidar\n"
        print(question6)
        print(options6)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question7 = "\n7)When US president Barack Obama visited India he made a reference to a popular Bollywood dialogue in his speech. What was the dialogue??"
        options7 = "  a. THAPPAD SE DARR NAHI LAGTA SAHIB, PYAAR SE LAGTA HAI\n  b. KITNE AADMI THE\n  c. SENORITA, BADE BADE DESHON MAIN AISI CHHOTI CHHOTI BAATEIN HOTI REHTI HAI\n  d. HOW’S THE JOSH?\n"
        print(question7)
        print(options7)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question8 = "\n8)Dil Chahta hai gave us some iconic dialogues like ‘Ya toh dosti gehri hai, ya toh yeh photo 3D hai’. Which character in the film says this line?"
        options8 = "  a. AAKASH\n  b. SAMEER\n  c. SIDDHARTH\n  d. ROHIT\n"
        print(question8)
        print(options8)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "b":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "b":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: b")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question9 = "\n9)Which song is inscribed at the back of the autorickshaw in 'Andhadhun'?"
        options9 = "  a. Yeh Jeewan Hai\n  b. Mud Mud Ke Na Dekh\n  c. Yeh Jo Mohabbat Hai\n  d. O Jaanewale\n"
        print(question9)
        print(options9)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "b":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "b":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: b")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question10 = "\n10)In 'Andaz Apna Apna', what's the name of the film that Juhi Chawla and Govinda are shooting for in Amar's dream?"
        options10 = "  a. Gulabi\n  b. Swarg\n  c. Aapka Karz\n  d. Pehra\n"
        print(question10)
        print(options10)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        print("\nYour Final score is "+str(score)+"/40")
        while True:
            if score == 40:
                print("Outstanding!!")
                break
            elif 31 <= score <= 39:
                print("Excellent!!")
                break
            elif 21 <= score <= 30:
                print("Good Work!!")
                break
            elif 11 <= score <= 20:
                print("Can do better!!")
                break
            else:
                print("Increase your knowledge :(")
                break
        break
    else:
        print("\n\n\t\tWelcome to General Knowledge Quiz:-")
        question1 = "\n1)Who is the brand ambassador of NOKIA Phones in India?"
        options1 = "  a. Shah Rukh Khan\n  b. Aamir Khan\n  c. Abhishek Bachchan\n  d. M.S. Dhoni\n"
        print(question1)
        print(options1)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")

                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")

                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question2 = "\n2)Which Indian State is the leading Cotton producer?"
        options2 = "  a. Gujarat\n  b. Maharashtra\n  c. Andhra Pradesh\n  d. Madhya Pradesh\n"
        print(question2)
        print(options2)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: \n")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: \n")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question3 = "\n3)Ball pen function on which one of the following principal?"
        options3 = "  a. Boyle’s law\n  b. Gravitational force\n  c. Surface tension\n  d. Viscosity\n"
        print(question3)
        print(options3)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question4 = "\n4)The Indian, who holds the pride of beating the computers in mathematical wizard is:"
        options4 = "  a. Shakuntala Devi\n  b. Raja Ramanna\n  c. Ramanujam\n  d. Rina Panigrahi\n"
        print(question4)
        print(options4)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
        
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question5 = "\n5)Microprocessor was invented by?"
        options5 = "  a. Alfred Nobel\n  b. Federico Faggin\n  c. Zacharias Janssen\n  d. Percy Spencer\n"
        print(question5)
        print(options5)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "b":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "b":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: b")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question6 = "\n6)NOS stands for _______?"
        options6 = "  a. Node operating system\n  b. Non-open software\n  c. Network Operating system\n  d. Non-operating software\n"
        print(question6)
        print(options6)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question7 = "\n7)Father of ‘C’ programming language?"
        options7 = "  a. Dennis Ritchie\n  b. Prof Jhon Kemeny\n  c. Thomas Kurtz\n  d. Bill Gates\n"
        print(question7)
        print(options7)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "a":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "a":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: a")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question8 = "\n8)Who was the first female to become the governor of an Indian state?"
        options8 = "  a. Subba Lakshmi\n  b. Padmaja Naidu\n  c. Sarojini Naidu\n  d. Vijaya Lakshmi Pandit\n"
        print(question8)
        print(options8)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question9 = "\n9)Who is the author of Devadas?"
        options9 = "  a. Indira Gandhi\n  b. Manu\n  c. Ravindra Nath Tagore\n  d. Sarat Chandra Chatterjee\n"
        print(question9)
        print(options9)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "d":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "d":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: d")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        question10 = "\n10)Author of The Diary of a young girl is?"
        options10 = "  a. Rachel Carson\n  b. Roland Barthes\n  c. Anne Frank\n  d. Ibn Battuta\n"
        print(question10)
        print(options10)
        while True:
            response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
            
            if response == "c":
                print("Correct!!!")
                score += 4
                break
            else:
                print("Incorrect!!! Try again.")
                
                while True:
                    response = input("Enter 'a', 'b', 'c' or 'd' for your answer: ")
                    
                    if response == "c":
                        print("Correct!!!")
                        stop = True
                        score += 4
                        break
                    else:
                        print("Incorrect!!! You ran out of your attempts")
                        print("Correct answer: c")
                        stop = True
                        score -= 1
                        break
                if stop:
                    break
        print("\nYour Final score is "+str(score)+"/40")
        while True:
            if score == 40:
                print("Outstanding!!")
                break
            elif 31 <= score <= 39:
                print("Excellent!!")
                break
            elif 21 <= score <= 30:
                print("Good Work!!")
                break
            elif 11 <= score <= 20:
                print("Can do better!!")
                break
            else:
                print("Increase your knowledge :(")
                break
        break
print('\n\n\t\tThank you for participating :)')
input()
