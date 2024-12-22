package studies.wsi.puzzle
package heuristics
import board.Board

import scala.util.control.NonLocalReturns.{returning, throwReturn}

trait RelaxableHeuristic extends BaseHeuristic  {
  def hasRowConflict(board: Board, y: Int, x: Int): Boolean = returning {
    val N =board.N
    val BLANK = 0
    var retValue: Boolean = false

    for (col1 <- 0 until N) {
      val k = board.get(y, col1)

      // check condition 4
      if !(BLANK == k) && getGoalY(N, k) == y then
        for (col2 <- col1 + 1 until N) {
          // check condition 1
          if col1 == x || col2 == x then
            val j = board.get(y, col2)

            // check condition 2
            if !(BLANK == j) && getGoalY(N, j) == y then
              if (getGoalX(N, j) < getGoalX(N, k)) {
                retValue = true
              } else {

              }
            else {

            }
          else {

          }
        }
    }
    retValue
  }
  def hasColConflict(board: Board, y: Int, x: Int): Boolean = returning {
    val N = board.N
    val BLANK = 0
    var retValue: Boolean = false

    for (row1 <- 0 until N) {
      val k = board.get(row1, x)

      // check condition 4
      if !(BLANK == k) && getGoalX(N, k) == x then
        for (row2 <- row1 + 1 until N) {
          // check condition 1
          if row1 == y || row2 == y then
            val j = board.get(row2, x)

            // check condition 2
            if !(BLANK == j) && getGoalX(N, j) == x then
              if getGoalY(N, j) < getGoalY(N, k) then
                retValue = true
              else {

              }
            else {

            }
          else {

          }

        }
      else {

      }
    }
    retValue
  }

  def hasConflict(board: Board, y: Int, x: Int): Boolean = {
    hasRowConflict(board, y, x) || hasColConflict(board, y, x)
  }

  def calculateFromPermutation(board: Board, relaxed: Boolean):Int
}
