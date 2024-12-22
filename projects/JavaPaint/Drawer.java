import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseWheelEvent;

/**
 *  Drawer 
 * Class that manages mouse listeners on Graphic panel that should draw figures
 * @see JGraphicPanel
 */
public class Drawer extends MouseAdapter {
    /**
     * graphic panel drawer is listening to
     */
    public JGraphicPanel gp;
    /**
     * Used during creation of figure. Tells how many points have we chosen yet. Used in Triangle and Rectangle
     */
    int clicks_in_action = 0;
    /**
     * Tells if we are during creation of a figure
     */
    boolean during_action;
    /**
     * Gives information about previous action
     */
    actType prev_action;
    /**
     * Gives information about action that is picked now
     */
    actType action;
    /**
     * Gives information about color that is picked now
     */
    Color color;
    /**
     * Gives information about previous color
     */
    Color prev_color;
    /**
     * Used during dragging. Point at which mouse was before refreshing
     */
    MyPoint prevDragPoint;
    /**
     * Figure that is being dragged
     */
    Figure figureDragged;

    /**
     * Constructor to initiate Drawer
     * @param gp graphic panel that drawer should listen to
     */
    public Drawer(JGraphicPanel gp) {
        this.gp = gp;
        resetAction();
        prev_action = actType.NONE;
        prev_color = null;
        action = actType.NONE;
        color = null;
        prevDragPoint = null;
        figureDragged = null;
    }

    /**
     * This method is used as a reset for mouseDragged
     */
    @Override
    public void mouseReleased(MouseEvent e) {
        System.out.println("Mouse has been released");
        prevDragPoint = null;
        figureDragged = null;
    }

    /**
     * Method used mainly to drag figures
     */
    @Override
    public void mouseDragged(MouseEvent e) {
        if (prevDragPoint == null) {
            prevDragPoint = new MyPoint(e.getX(), e.getY());
        }
        MyPoint dragPoint = new MyPoint(e.getX(), e.getY());
        if (action == actType.PICK) {
            if (figureDragged == null) {
                Figure tempToDrag = null;

                for (Figure figure : gp.Figures) {
                    if (figure.contains(new MyPoint(e.getX(), e.getY())) && figure.priority == Figure.max_priority) {
                        tempToDrag = figure;
                    }
                }
                figureDragged = tempToDrag;
            }
            if (figureDragged != null) {
                figureDragged.drag(prevDragPoint, dragPoint);
            }
        }
        gp.repaint();
        prevDragPoint.mutate_to(dragPoint);
    }

    /**
     * During creation of figure, moving mouse should change shape of figure
     */
    @Override
    public void mouseMoved(MouseEvent e) {
        if (during_action) {
            if (action == actType.CIRCLE || action == actType.TRIANGLE || action == actType.RECTANGLE) {
                assert gp.tempBaseFigure != null;
                gp.tempBaseFigure.changeDuringCreation(new MyPoint(e.getX(), e.getY()));
            }
            gp.repaint();
        }
    }

    /**
     * Method used to resize changed figure
     */
    @Override
    public void mouseWheelMoved(MouseWheelEvent e) {
        if (action == actType.PICK) {
            Figure tempToResize = null;
            for (Figure figure : gp.Figures) {
                if (figure.contains(new MyPoint(e.getX(), e.getY())) && figure.priority == Figure.max_priority) {
                    tempToResize = figure;
                }
            }

            if (tempToResize != null) {
                if (e.getWheelRotation() == 1) {
                    tempToResize.resizeSmaller();
                } else {
                    tempToResize.resizeBigger();
                }
            }
            gp.repaint();
        }
    }

    /**
     * Method that handles many actions that should be possible by clicking mouse
     * If if click was RightMouseButton and it was on created Figure it will call frame to change colors of figure
     * By using action like Triangle, Rectangle, Circle by clicking u are able to make figures
     * By using action like Pick or Delete u can raise priority of figure or delete figure
     */
    public void mouseClicked(MouseEvent e) {
        if (SwingUtilities.isLeftMouseButton(e)) {
            if (action == actType.DELETE) {
                Figure tempToDelete = null;
                int tempPriority = 0;
                for (Figure figure : gp.Figures) {
                    if (figure.contains(new MyPoint(e.getX(), e.getY())) && figure.priority > tempPriority) {
                        tempToDelete = figure;
                        tempPriority = figure.priority;
                    }
                }
                if (tempPriority != 0) {
                    System.out.println("Decided to delete is " + tempToDelete.color.toString() + " " + tempToDelete.name + " with priority " + tempToDelete.priority + ".");
                    if (gp.colorChangeFrame != null) {
                        if (tempToDelete == gp.colorChangeFrame.figure) {
                            gp.colorChangeFrame.dispose();
                            gp.colorChangeFrame = null;
                        }
                    }
                    gp.Figures.remove(tempToDelete);
                }
            } else if (action == actType.PICK) {
                Figure tempToPick = null;
                int tempPriority = 0;
                for (Figure figure : gp.Figures) {
                    if (figure.contains(new MyPoint(e.getX(), e.getY())) && figure.priority > tempPriority) {
                        tempToPick = figure;
                        tempPriority = figure.priority;
                    }
                }
                if (tempPriority != 0) {
                    System.out.println("Decided to pick is " + tempToPick.color.toString() + " " + tempToPick.name + " with priority " + tempToPick.priority + ".");
                    Figure.max_priority += 1;
                    tempToPick.priority = Figure.max_priority;
                }
            } else if (!(color == null || action == actType.NONE)) {
                if (!during_action) {
                    during_action = true;
                    switch (action.toString()) {
                        case "CIRCLE" -> gp.tempBaseFigure = new Circle(e.getX(), e.getY(), 0, color);
                        case "RECTANGLE", "TRIANGLE" -> {
                            gp.tempBaseFigure = new Line(new MyPoint(e.getX(), e.getY()), null, color);
                            clicks_in_action += 1;
                        }
                        default -> System.out.println("Action without proper name provided");
                    }
                } else {
                    if (action == actType.CIRCLE || (action == actType.RECTANGLE && clicks_in_action == 2) || (action == actType.TRIANGLE && clicks_in_action == 2)) {
                        Figure tempFigure = (Figure) gp.tempBaseFigure;
                        tempFigure.created();
                        gp.Figures.add((Figure) gp.tempBaseFigure);
                        System.out.println(color.toString() + " " + action.toString() + " Priority: " + ((Figure) gp.tempBaseFigure).priority + " Drawn. ");
                        resetAction();

                    } else if (action == actType.TRIANGLE && clicks_in_action == 1) {
                        Line line = (Line) gp.tempBaseFigure;
                        gp.tempBaseFigure = new Triangle(line.creator, line.finisher, null, color);
                        clicks_in_action += 1;
                    } else if (action == actType.RECTANGLE && clicks_in_action == 1) {
                        Line line = (Line) gp.tempBaseFigure;
                        gp.tempBaseFigure = new Rectangle(line.creator, line.finisher, null, null, color);
                        clicks_in_action += 1;
                    } else {
                        System.out.println("action or clicks not controlled by ifs " + action + " " + clicks_in_action);
                    }
                }
            }
        }
        if (SwingUtilities.isRightMouseButton(e)) {
            Figure tempToChangeColor = null;
            int tempPriority = 0;
            for (Figure figure : gp.Figures) {
                if (figure.contains(new MyPoint(e.getX(), e.getY())) && figure.priority > tempPriority) {
                    tempToChangeColor = figure;
                    tempPriority = figure.priority;
                }
            }
            if (tempPriority != 0) {
                System.out.println("Decided to changeColor is " + tempToChangeColor + " " + tempToChangeColor.name + " with priority " + tempToChangeColor.priority + ".");
                if (gp.colorChangeFrame != null) {
                    gp.colorChangeFrame.dispose();
                    gp.colorChangeFrame = null;
                }
                gp.colorChangeFrame = new JColorChangeFrame(tempToChangeColor, gp);
            }
        }

        gp.repaint();
    }

    /**
     * Method used to reset action after creating a figure by MouseClicked
     */
    public void resetAction() {
        gp.tempBaseFigure = null;
        during_action = false;
        clicks_in_action = 0;
    }
}

