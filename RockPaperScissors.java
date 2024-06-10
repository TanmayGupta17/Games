import java.util.*;

public class RockPaperScissors {
    RockPaperScissors() {
        Scanner sc = new Scanner(System.in);
        String arr[] = { "Rock", "Paper", "Scissors" };

        System.out.println("Enter no of rounds: ");
        int n = sc.nextInt();
        System.out.println("Welcome!!!");
        System.out.println("In this game you have to beat the bot in the game of rock paper scissors");
        System.out.println("Whoever wins the best of " + n + " wins the game");
        System.out.println("May the best player wins");
        System.out.println();
        int i = 0;
        int playerscore = 0;
        int botscore = 0;
        while (i < n) {
            System.out.println("Enter any one of the options\nRock\nPaper\nScissors");
            System.out.print("Enter your move: ");
            String s = sc.next();
            Random r = new Random();
            int randoNo = r.nextInt(arr.length - 1);
            // System.out.println(arr[randoNo]);
            if (s.equals("Scissors") && arr[randoNo].equals("Rock")) {
                System.out.println("Bot: " + arr[randoNo]);
                botscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.equals("Paper") && arr[randoNo].equals("Scissors")) {
                System.out.println("Bot: " + arr[randoNo]);
                botscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.equals("Rock") && arr[randoNo].equals("Paper")) {
                System.out.println("Bot: " + arr[randoNo]);
                botscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.equals("Paper") && arr[randoNo].equals("Rock")) {
                System.out.println("Bot: " + arr[randoNo]);
                playerscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.equals("Scissors") && arr[randoNo].equals("Paper")) {
                System.out.println("Bot: " + arr[randoNo]);
                playerscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.equals("Rock") && arr[randoNo].equals("Scissors")) {
                System.out.println("Bot: " + arr[randoNo]);
                botscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.equals("Scissors") && arr[randoNo].equals("Rock")) {
                System.out.println("Bot: " + arr[randoNo]);
                botscore++;
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            } else if (s.compareTo(arr[randoNo]) == 0) {
                System.out.println("Bot: " + arr[randoNo]);
                System.out.println("It's a tie");
                System.out.println("Bot Score: " + botscore);
                System.out.println("Player Score: " + playerscore);
                System.out.println();
                i++;
            }
            if (playerscore > n / 2 || botscore > n / 2) {
                break;
            }
        }
        if (playerscore > botscore) {
            System.out.println("Congratulations!!");
            System.out.println("You won");
        } else if (playerscore == botscore) {
            System.out.println("It's a tie");
            System.out.println("Try Again");
        }

        else {
            System.out.println("Better Luck Next Time :(");
        }
    }

    public static void main(String[] args) {
        RockPaperScissors rps = new RockPaperScissors();
    }
}
