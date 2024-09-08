// Randomly generate numbers between 1 and 1000 for user to guess.
#include <iostream>
#include <random> // contains C++11 random number generation features 
using namespace std;

bool isCorrect(int, int); // function prototype

int main() {
   // use the default random-number generation engine to                
   // produce uniformly distributed pseudorandom int values from 1 to 1000
   default_random_engine engine{random_device{}()};
   uniform_int_distribution<int> randomInt{1, 1000};

   char response = 'n'; // determines whether to continue playing

   // loop until user types 'n' to quit game
   do {
      // generate random number between 1 and 1000
      // 1 is shift, 1000 is scaling factor
      const int answer{randomInt(engine)};

      // prompt for guess
      cout << "I have a number between 1 and 1000.\n"
         << "Can you guess my number?\n"
         << "Please type your first guess." << endl << "? ";
      int guess;
      cin >> guess;

      // loop until correct number
      while (!isCorrect(guess, answer)) {
         cin >> guess;
      }

      // prompt for another game
      cout << "\nExcellent! You guessed the number!\n"
         << "Would you like to play again (y or n)? ";
      cin >> response;

      cout << endl;
   } while (response == 'y');

   return 0; // indicate successful termination
} 

// isCorrect returns true if guess equals answer;
// otherwise it displays a hint and returns false
bool isCorrect(int guess, int answer) {
   // guess is correct
   if (guess == answer) {
      return true;
   }

   // guess is incorrect; display hint
   if (guess < answer) {
      cout << "Too low. Try again.\n? ";
   }
   else {
      cout << "Too high. Try again.\n? ";
   }

   return false;
} // end function isCorrect