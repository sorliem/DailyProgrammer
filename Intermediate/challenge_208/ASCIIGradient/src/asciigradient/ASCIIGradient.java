package asciigradient;

import java.util.Scanner;

/**
 *
 * @author sorliem
 */
public class ASCIIGradient {

    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int width = in.nextInt();
        int height = in.nextInt();
        String gradientChars = in.nextLine();
        char gradient[] = gradientChars.toCharArray();
        String fill = in.next();
        if (fill == "raidal") {
            int startX = in.nextInt();
            int startY = in.nextInt();
            int radius = in.nextInt();
        } else {
            // fill is linear
            int startX = in.nextInt();
            int startY = in.nextInt();
            int endX = in.nextInt();
            int endY = in.nextInt();
        }

        // Not done.
        
    }

}
