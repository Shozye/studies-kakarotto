package studies.wsi.puzzle
package heuristics

import board.Board

object ManhattanDistanceHeuristics extends Heuristic {
  private def taxicabDistance(x1: Int, y1: Int, x2: Int, y2: Int): Int = {
    math.abs(x1 - x2) + math.abs(y1 - y2)
  }

  override def calculateFromPermutation(board: Board): Int = {
    val n = board.N
    val tiles = board.board

    var distance = 0
    for (i <- tiles.indices) {
      if (tiles(i) != 0) {
        val row = i / n
        val col = i % n
        val targetRow = (tiles(i) - 1) / n
        val targetCol = (tiles(i) - 1) % n
        distance += taxicabDistance(row, col, targetRow, targetCol)
      }
    }
    distance
  }

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = ???
}
