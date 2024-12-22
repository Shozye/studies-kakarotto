package studies.wsi.puzzle
package heuristics

import studies.wsi.puzzle.board.Board

object InversionDistanceHeuristics extends Heuristic {
  override def calculateFromPermutation(board: Board): Int = ???

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = ???
}
