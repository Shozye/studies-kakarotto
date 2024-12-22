package strategies

object StrategyUtils {
    def min(a: Int, b: Int): Double = if (a > b) b else a
    def max(a: Int, b: Int): Double = if (a > b) a else b
    def min(a: Double, b: Double): Double = if (a > b) b else a
    def max(a: Double, b: Double): Double = if (a > b) a else b

    def min(a: Double, b: Int): Double = if (a > b) b else a
    def max(a: Double, b: Int): Double = if (a > b) a else b
    def min(a: Int, b: Double): Double = if (a > b) b else a
    def max(a: Int, b: Double): Double = if (a > b) a else b
}
