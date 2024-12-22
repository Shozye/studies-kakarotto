import javax.swing.*;
import java.awt.*;

/**
 *  JActionButton 
 * Button with photo
 */
public class JActionButton extends JButton {
    /**
     * icon that will be shown on button
     */
    ImageIcon icon;
    /**
     * path to icon
     */
    String iconPath;
    /**
     * action type that button is representing
     */
    actType action_type;

    /**
     *
     * @param iconPath path to icon
     * @param width width of button
     * @param height height of button
     * @param action_type action type that button is representing
     */
    public JActionButton(String iconPath, int width, int height, actType action_type) {
        super(null, new ImageIcon(iconPath));
        this.action_type = action_type;
        this.icon = new ImageIcon(iconPath);
        this.iconPath = iconPath;
        this.setPreferredSize(new Dimension(width, height));
    }
}

