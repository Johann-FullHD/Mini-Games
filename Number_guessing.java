import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int numberToGuess = random.nextInt(10) + 1; // generates a random number between 1 and 10
        int guess;
        int attempts = 0;

        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("I have generated a random number between 1 and 10.");
        System.out.println("Can you guess what it is?");

        do {
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            attempts++;

            if (guess < numberToGuess) {
                System.out.println("Too low! Try again.");
            } else if (guess > numberToGuess) {
                System.out.println("Too high! Try again.");
            }
        } while (guess != numberToGuess);

        System.out.println("Congratulations! You have correctly guessed the number in " + attempts + " attempts.");
    }
}
