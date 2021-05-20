import javax.swing.*;
import java.awt.*;

/**
 *  JHelpFrame 
 * Class that is a JFrame that gives information about how to use JavaPaint
 */
public class JHelpFrame extends JFrame {

    /**
     * Constructor for help frame
     */
    public JHelpFrame() {
        JPanel panel;
        JLabel label1;
        JLabel label2;
        JLabel label3;
        JLabel label4;
        JTextPane textPane1;
        JTextPane textPane2;
        JTextPane textPane3;
        JTextPane textPane4;

        setTitle("Info");
        panel = new JPanel();
        this.add(panel);
        panel.setPreferredSize(new Dimension(500, 325));
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        label1 = new JLabel();
        label1.setAlignmentX(CENTER_ALIGNMENT);
        label1.setBackground(panel.getBackground());
        label1.setText("Tworzenie");
        textPane1 = new JTextPane();
        textPane1.setBackground(panel.getBackground());
        textPane1.setText("By stworzyc figure nalezy wybrac akcje i kolor z gornego panelu a nastepnie \n w przypadku wyboru okregu nalezy klikajac wybrac dwa punkty tworzace okrag \n w przypadku prostokata i trojkata nalezy pierw wybrac dwa punkty tworzace podstawe a pozniej trzeci punkt tworzacy figure \n Wszystkie wybory zatwierdzamy lewym przyciskiem myszy");
        textPane1.setEditable(false);
        label2 = new JLabel();
        label2.setAlignmentX(CENTER_ALIGNMENT);
        label2.setBackground(panel.getBackground());
        label2.setText("Usuwanie");
        textPane2 = new JTextPane();
        textPane2.setBackground(panel.getBackground());
        textPane2.setText("By usunac figure wystarczy wybrac z gornego panelu opcje z czerwonym przyciskiem i kliknac na figure ktora chcemy usunac lewym przyciskiem myszy");
        textPane2.setEditable(false);
        label3 = new JLabel();
        label3.setAlignmentX(CENTER_ALIGNMENT);
        label3.setBackground(panel.getBackground());
        label3.setText("Modyfikowanie figur");
        textPane3 = new JTextPane();
        textPane3.setBackground(panel.getBackground());
        textPane3.setText("By zmienic kolor juz istniejacej figury wystarczy kliknac na nia prawym przyciskiem myszy i zmienic kolor z nowego okna. \n By przesuwac lub powiekszac figury nalezy pierw w gornym panelu wybrac pierwsza akcje z kursorem, nastepnie wybrac figure LPM i pozniej mozna ja przesuwac oraz zwiekszac lub pomniejszac scrollem");
        textPane3.setEditable(false);
        label4 = new JLabel();
        label4.setAlignmentX(CENTER_ALIGNMENT);
        label4.setBackground(panel.getBackground());
        label4.setText("Zapisywanie i wczytywanie");
        textPane4 = new JTextPane();
        textPane4.setBackground(panel.getBackground());
        textPane4.setText("By zapisac lub wczytac figure nalezy wybrac z menu glownego opcje Save lub Load");
        textPane4.setEditable(false);

        panel.add(label1);
        panel.add(textPane1);
        panel.add(label2);
        panel.add(textPane2);
        panel.add(label3);
        panel.add(textPane3);
        panel.add(label4);
        panel.add(textPane4);

        this.setVisible(true);
        this.setResizable(false);

        this.pack();
    }
}
