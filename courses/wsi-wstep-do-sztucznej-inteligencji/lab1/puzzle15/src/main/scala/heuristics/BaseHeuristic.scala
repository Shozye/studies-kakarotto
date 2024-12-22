package studies.wsi.puzzle
package heuristics

trait BaseHeuristic {
  val BLANK = 0
  def getGoalX(N: Int, tile: Int): Int = {
    if (tile == BLANK) {
      N - 1
    } else {
      (tile - 1) % N
    }
  }

  def getGoalY(N: Int, tile: Int): Int = {
    if (tile == BLANK) {
      N - 1
    } else {
      (tile - 1) / N
    }
  }

  def getGoalTile(N: Int, y: Int, x: Int): Int = {
    if x == y && y == N-1 then
      BLANK
    else {
      (N * y) + x + 1
    }
  }
}
