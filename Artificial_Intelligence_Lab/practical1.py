from experta import *

# Fact class to store student interests
class StudentFacts(Fact):
    pass

# Expert system definition
class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

# Main function
def main():
    engine = CareerExpertSystem()
    engine.reset()  # prepare the engine for running
    print("Welcome to the Career Path Expert System!")
    
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    
    engine.run()

# Entry point
if __name__ == "__main__":
    main()

