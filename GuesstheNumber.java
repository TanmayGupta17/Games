import java.util.Random;
import java.util.Scanner;

class GuesstheNumber {
    public static void Game() {
        Scanner sc = new Scanner(System.in);
        int count = 5;
        Random rand = new Random();
        int upperlimit = 100;
        int i;
        int r = rand.nextInt(upperlimit);
        System.out.println("Guess a the number" + "Number is between 0 and 100");
        System.out.println("You have 5 attempts to guess the number");
        System.out.println("All the best!!");
        for (i = 0; i < count; i++) {
            int guess = sc.nextInt();
            if (guess < r) {
                System.out.println("Try a bigger number");
            } else if (guess > r) {
                System.out.println("Try a smaller number");
            } else if (guess == r) {
                System.out.println("Congratulations You have guessed the number\n" + "You are a genius");
                break;
            }
        }
        System.out.println();
        if (i == count) {
            System.out.println("You have exhausted all Your chances");
            System.out.println("Better luck next time");
            System.out.println();
            System.out.println("The no was " + r);
        }
    }

    public static void main(String[] args) {
        Game();
    }
}