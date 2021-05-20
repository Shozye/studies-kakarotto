import javax.swing.*;
import java.awt.*;

/**
 *  Logo 
 * Class to handle JPanel that is fully filled with icon
 */
public class Logo extends JPanel {
    /**
     * Image shown on JPanel
     */
    private Image img;

    /**
     * Constructor for Logo
     * @param width width of panel
     * @param height height of panel
     */
    public Logo(int width, int height) {
        setBorder(BorderFactory.createLineBorder(Color.black, 2, false));
        this.setPreferredSize(new Dimension(width, height));
    }

    /**
     * Method to change image that is currently shown
     * @param icon icon which will be shown
     */
    public void changeImage(ImageIcon icon) {
        this.img = icon.getImage();
        repaint();
    }

    /**
     * Method to draw image on panel
     */
    public void paintComponent(Graphics g) {
        g.drawImage(img, -10, -10, null);
    }

}
