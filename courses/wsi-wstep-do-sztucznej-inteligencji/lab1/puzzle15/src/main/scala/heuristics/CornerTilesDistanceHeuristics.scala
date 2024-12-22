package studies.wsi.puzzle
package heuristics
import board.Board

object CornerTilesDistanceHeuristics extends RelaxableHeuristic {
  private def checkAdjacent(board: Board, yx: (Int, Int), N: Int, relaxed: Boolean): Int = {
    val (y, x) = yx
    val adj = getGoalTile(N, y, x)
    if adj != board.get(y, x) ||
        (!relaxed && hasConflict(board, y, x)) then
      0
    else
      2
  }

  private def checkCorner(board: Board, y: Int, x: Int, adj1: (Int, Int), adj2: (Int, Int), N: Int, relaxed: Boolean): Int = {
    val corner = getGoalTile(N, y, x)
    if BLANK != board.get(y, x) && corner != board.get(y,x) then
      checkAdjacent(board, adj1, N, relaxed) + checkAdjacent(board, adj2, N, relaxed)
    else
      0
  }

  override def calculateFromPermutation(board: Board, relaxed: Boolean): Int = {
    val N = board.N
    if N < 4 then
      0
    else {
      var dist = 0
      dist += checkCorner(board, 0, 0, (0, 1), (1, 0), N, relaxed)
      dist += checkCorner(board, 0, N - 1, (0, N - 2), (1, N - 1), N, relaxed)
      dist += checkCorner(board, N - 1, 0, (N - 1, 1), (N - 2, 0), N, relaxed)
      dist
    }

  }
}
