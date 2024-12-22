package studies.wsi.puzzle
package heuristics
import board.Board

object ManhattanLinearConflictsHeuristics extends Heuristic {
  override def calculateFromPermutation(board: Board): Int = {
    ManhattanDistanceHeuristics.calculateFromPermutation(board) +
      LinearConflictsHeuristics.calculateFromPermutation(board)
  }

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = ???
}
