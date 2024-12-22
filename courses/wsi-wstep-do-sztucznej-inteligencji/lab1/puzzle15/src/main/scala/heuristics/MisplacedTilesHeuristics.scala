package studies.wsi.puzzle
package heuristics

import board.Board

object MisplacedTilesHeuristics extends Heuristic {
  override def calculateFromPermutation(board: Board): Int = {
    var amountMisplaced = board.board.length
    
    for i <- board.board.indices do {
      if (board.board(i) == (i+1) % board.board.length){
        amountMisplaced -= 1
      }
    }
    amountMisplaced
  }

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = {
    0
  }
}
