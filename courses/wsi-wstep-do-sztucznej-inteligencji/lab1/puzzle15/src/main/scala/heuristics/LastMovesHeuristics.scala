package studies.wsi.puzzle
package heuristics
import board.Board

object LastMovesHeuristics extends RelaxableHeuristic {
  override def calculateFromPermutation(board: Board, relaxed: Boolean): Int = {
    val N = board.N

    val adj1 = getGoalTile(N, N-2, N-1)
    val adj2 = getGoalTile(N, N-1, N-2)
    val corner = board.get(N-1, N-1)

    if corner == adj1 || corner == adj2 || board.isSolved then
      0
    else if (!relaxed) {
      val (adj1_y, adj1_x) = board findTile adj1
      val (adj2_y, adj2_x) = board findTile adj2
      // prevent interaction with Manhattan
      if adj1_y > N - 2 || adj2_x > N - 2 then
         0
      //prevent interaction with linear conflict distance
      else if adj1_y == N - 2 && hasRowConflict(board, adj1_y, adj1_x) then
         0
      else if  adj2_x == N - 2 && hasColConflict(board, adj2_y, adj2_x) then
         0
      else
        2
    } else {
      2
    }
  }
}
