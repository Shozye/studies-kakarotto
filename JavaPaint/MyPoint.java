/**
 *  MyPoint 
 * Class used to handle points in basefigures
 * @see BaseFigure
 */
public class MyPoint {
    /**
     * x value rounded from rx
     */
    int x;
    /**
     * y value rounded from ry
     */
    int y;
    /**
     * real value of x of point
     */
    double rx;
    /**
     * real value of y of point
     */
    double ry;

    /**
     * Constructor to create point from integers
     * @param x x of point
     * @param y y of point
     */
    public MyPoint(int x, int y) {
        update(x, y);
    }

    /**
     * Constructor to create point from doubles
     * @param rx real x of point
     * @param ry real y of point
     */
    public MyPoint(double rx, double ry) {
        update(rx, ry);
    }

    /**
     * Constructor to create point from another point
     * @param p point from which we are creating another point
     */
    public MyPoint(MyPoint p) {
        update(p.rx, p.ry);
    }

    /**
     * Method to change point into another point
     * @param a point into we are changing
     */
    public void mutate_to(MyPoint a) {
        update(a.rx, a.ry);
    }

    /**
     * Method to calculate distance squared to other point
     * @param p other point
     * @return range from this to p squared
     */
    public double distancesq_to(MyPoint p) {
        return ((rx - p.rx) * (rx - p.rx) + (ry - p.ry) * (ry - p.ry));
    }

    /**
     * Method to change x, y values of point
     * @param real_x new x of point
     * @param real_y new y of point
     */
    public void update(double real_x, double real_y) {
        this.ry = real_y;
        this.rx = real_x;
        this.x = (int) real_x;
        this.y = (int) real_y;
    }

    /**
     * Method to calculate where should be point after
     * cook-off from p by how_much
     * @param p point from which we are doing cook-off
     * @param how_much factor of cook-off
     */
    public void move_away_from(MyPoint p, double how_much) {

        double temprx = how_much * (rx - p.rx) + p.rx;
        double tempry = how_much * (ry - p.ry) + p.ry;
        update(temprx, tempry);
    }

    /**
     * Only for debugging purposes
     */
    @Override
    public String toString() {
        return "Pt{x:" + x + " y:" + y + "}";
    }

}
