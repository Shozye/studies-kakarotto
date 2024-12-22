package studies.wsi.puzzle
package game

import board.Board

object SolverUtils {
  def inverts(board: Board): Int = {
    (for {
      i <- 0 until board.N*board.N
      j <- i + 1 until board.N*board.N
      if board.board(i) != 0 && board.board(j) != 0
    } yield board.board(i) > board.board(j))
      .count(_ == true)
  }

  def isSolvable(board: Board): Boolean = {
    (
      inverts(board) +
      (board.N % 2 match
        case 0 => board.N - 1 - board.empty(0)
        case _ => 0
      )
    ) % 2 == 0
  }

}
