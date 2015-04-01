package avatarbuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Date: 8/6/14
 * @author sorliem143
 */
public class AvatarBuilder {

    
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("avatar.in"));
        String[] names = in.nextLine().split(" ");
        for (int i = 0; i < names.length; i++) {
            String userName = names[i];
            int charTotal = 0;
            char[][] image = new char[10][10];
            for (int j = 0; j < userName.length(); j++) {
                charTotal += (int) userName.charAt(j);
            }
            for (int j = 2; j < 12; j++) {
                int leftOver = charTotal % j;
                String bin = Integer.toBinaryString(leftOver);
                for (int k = 0; k < bin.length(); k++) {
                    image[j-2][k] = bin.charAt(k);
                    image[j-2][9-k] = bin.charAt(k);
                }
            }
            System.out.println("Avatar for " + userName );
            generateAvatar(image);
        }
    }
    
    private static void generateAvatar(char[][] img) {
        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                if (img[i][j] == '1') {
                    System.out.print("#");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println("");
        }
    }
}
