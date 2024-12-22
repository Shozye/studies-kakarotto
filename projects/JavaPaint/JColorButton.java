import javax.swing.*;
import java.awt.*;

/**
 *  JColorButton 
 * Class creating button with certain color used in
 * @see JColorPanel
 */
public class JColorButton extends JButton {
    /**
     * color of button
     */
    Color color;

    /**
     * constructor for Color Button
     * @param color color of button
     * @param width width of button
     * @param height height of button
     */
    public JColorButton(Color color, int width, int height) {
        this.setBackground(color);
        this.color = color;
        this.setPreferredSize(new Dimension(width, height));
    }
}
