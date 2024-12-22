package studies.wsi.puzzle
package heuristics

import studies.wsi.puzzle.board.Board

trait Heuristic extends BaseHeuristic {
  def calculateFromPermutation(board: Board): Int
  def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int
}
