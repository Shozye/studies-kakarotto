import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *  JColorPanel 
 * Class that contains 8 buttons with colors and also
 * contains panel that shows color of last picked button
 * It is used in JInputPanel and in JColorChangeFrame
 * @see JColorButton
 * @see JInputPanel
 */
public class JColorPanel extends JPanel {
    /**
     * list with color buttons
     */
    JColorButton[] buttons = new JColorButton[8];
    /**
     * Panel that show color of picked color
     */
    JPanel picked = new JPanel();
    /**
     * placeholder
     */
    JPanel blank = new JPanel();

    /**
     * Creator of Color Panel
     * @param width width of panel
     * @param height height of panel
     */
    public JColorPanel(int width, int height) {
        this.setBorder(BorderFactory.createLineBorder(Color.ORANGE, 2, true));
        this.setPreferredSize(new Dimension(width, height));
        this.setLayout(new GridLayout(2, 5));
        ColorShowActionListener picked_listener = new ColorShowActionListener();
        Color[] colors = new Color[]{Color.black, Color.blue, Color.red, Color.magenta, Color.green, Color.cyan, Color.yellow, Color.white};
        for (int i = 0; i < 8; i++) {
            buttons[i] = new JColorButton(colors[i], height / 2, height / 2);
            buttons[i].addActionListener(picked_listener);
        }
        this.add(picked);
        for (int i = 0; i < 4; i++) {
            this.add(buttons[i]);
        }
        this.add(blank);
        for (int i = 4; i < 8; i++) {
            this.add(buttons[i]);
        }
        Dimension size = new Dimension(height / 2, height / 2);
        picked.setPreferredSize(size);
        picked.setBorder(BorderFactory.createLineBorder(Color.black, 5, true));
        blank.setPreferredSize(size);
    }

    /**
     * Class that listens to click of color button and sets color of panel to
     * the color of clicked button
     */
    class ColorShowActionListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            JColorButton temp = (JColorButton) e.getSource();
            picked.setBackground(temp.color);
        }
    }

}
