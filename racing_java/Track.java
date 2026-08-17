import java.awt.*;
import javax.swing.*; 

public class Track {
    private static void createTrack(){
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(200,200);
        frame.setVisible(true);
        frame.getContentPane().setBackground(Color.BLACK);
    }

    public static void main(String[] args){
    createTrack();

}
    
}

