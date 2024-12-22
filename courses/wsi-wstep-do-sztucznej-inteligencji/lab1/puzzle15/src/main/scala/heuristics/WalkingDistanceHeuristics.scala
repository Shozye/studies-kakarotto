package studies.wsi.puzzle
package heuristics

import studies.wsi.puzzle.board.Board

object WalkingDistanceHeuristics extends Heuristic {
  override def calculateFromPermutation(currentBoard: Board): Int = ???

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = ???
}
