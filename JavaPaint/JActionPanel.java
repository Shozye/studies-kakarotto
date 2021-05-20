import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *  JActionPanel 
 * Class containing ActionButtons that give information about what action is picked
 * Picked information is shown in Logo
 * @see Logo
 * @see JActionButton
 */
public class JActionPanel extends JPanel {
    /**
     * Logo class on which there is an icon showing what action has been chosen
     */
    Logo picked;
    /**
     * Shows what action picked represents
     */
    actType pickedInfo;
    /**
     * List containing action buttons
     */
    JActionButton[] actionButtons = new JActionButton[5];

    /**
     * Constructor for Action panel
     * @param width width of action panel
     * @param height height of action panel
     */
    @SuppressWarnings("SuspiciousNameCombination")
    public JActionPanel(int width, int height) {
        this.setBorder(BorderFactory.createLineBorder(Color.black, 5, true));
        this.setPreferredSize(new Dimension(width, height));
        this.setLayout(new GridLayout(1, 6));
        picked = new Logo(height, height);
        this.add(picked);
        actionButtons[0] = new JActionButton("src/photos/pick.png", height, height, actType.PICK);
        actionButtons[1] = new JActionButton("src/photos/triangle.png", height, height, actType.TRIANGLE);
        actionButtons[2] = new JActionButton("src/photos/rect.png", height, height, actType.RECTANGLE);
        actionButtons[3] = new JActionButton("src/photos/circle.png", height, height, actType.CIRCLE);
        actionButtons[4] = new JActionButton("src/photos/del.png", height, height, actType.DELETE);
        PickShowActionListener action_changer = new PickShowActionListener();
        for (int i = 0; i < 5; i++) {
            this.add(actionButtons[i]);
            actionButtons[i].addActionListener(action_changer);
        }
    }

    /**
     *  pickShowActionListener 
     * Class that changes image of picked panel after
     * click to JActionButton
     */
    class PickShowActionListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            JActionButton temp = (JActionButton) e.getSource();
            picked.changeImage(temp.icon);
            pickedInfo = temp.action_type;
        }
    }
}
