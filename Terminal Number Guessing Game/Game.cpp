#include <iostream>
#include <ctime>


void PrintIntroduction(int Difficulty)
{
    // Print intro messages
    std::cout << "\n\nYou are a hacker breaking into a Level " << Difficulty << " secure server room..." << std::endl;
    std::cout << "You need to enter the correct code to continue..\n" << std::endl;
    
}

bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);

    // Declare 3 number codes
    const int CodeA = rand() % Difficulty + Difficulty;
    const int CodeB = rand() % Difficulty + Difficulty;
    const int CodeC = rand() % Difficulty + Difficulty;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;

    // Print sum and product
    std::cout << std::endl;
    std::cout << "There are 3 numbers in the code";
    std::cout << "\n+The codes add-up to: " << CodeSum;
    std::cout << "\n+The codes multiply to give: " << CodeProduct << std::endl;

    // Player Guess
    int GuessA, GuessB, GuessC;
    std::cin >> GuessA >> GuessB >> GuessC;

    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    // Check if player entered correct
    if (GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "\n*** Well done! You extracted a file, keep going! ***";
        return true;
    }
    else
    {
        std::cout << "\n*** You entered the wrong code! Be careful and try again! ***";
        return false;
    }

}

int main()
{  
    srand(time(NULL)); // Create random sequence based on computers time

    int LevelDifficulty = 1;
    int const MaxDifficulty = 5;

    while (LevelDifficulty <= MaxDifficulty) // Loop the game until all levels completed
    {
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear();
        std::cin.ignore();

        if (bLevelComplete)
        {
            ++LevelDifficulty;
        }
    }

    std::cout << "\n*** Well done agent, you extracted all the files! ***";

    return 0;
}