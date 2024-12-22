import javax.swing.*;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;
import java.awt.*;

/**
 *  JInfoFrame 
 * Class containing frame with information of creator and objective of program
 */
public class JInfoFrame extends JFrame {

    /**
     * Base constructor of infoframe
     */
    public JInfoFrame() {
        JPanel panel;
        JTextPane textPane;

        setTitle("Info");
        panel = new JPanel();
        this.add(panel);
        textPane = new JTextPane();
        textPane.setBackground(panel.getBackground());
        textPane.setPreferredSize(new Dimension(200, 100));
        textPane.setText("LepszyPaint \n Autor: Mateusz Pełechaty \n\n Program stworzony na zajęcia kursu programowania na Politechnice Wrocławskiej");
        StyledDocument doc = textPane.getStyledDocument();
        SimpleAttributeSet center = new SimpleAttributeSet();
        StyleConstants.setAlignment(center, StyleConstants.ALIGN_CENTER);
        doc.setParagraphAttributes(0, doc.getLength(), center, false);

        textPane.setEditable(false);
        panel.add(textPane);
        this.setVisible(true);
        this.setResizable(false);

        this.pack();
    }
}
