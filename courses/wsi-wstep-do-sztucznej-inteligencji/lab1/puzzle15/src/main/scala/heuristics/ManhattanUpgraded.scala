package studies.wsi.puzzle
package heuristics
import board.Board

object ManhattanUpgraded extends Heuristic {
  override def calculateFromPermutation(board: Board): Int = {
    ManhattanDistanceHeuristics.calculateFromPermutation(board) +
      LinearConflictsHeuristics.calculateFromPermutation(board) +
      LastMovesHeuristics.calculateFromPermutation(board, false) +
      CornerTilesDistanceHeuristics.calculateFromPermutation(board, false)
  }

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = ???
}
