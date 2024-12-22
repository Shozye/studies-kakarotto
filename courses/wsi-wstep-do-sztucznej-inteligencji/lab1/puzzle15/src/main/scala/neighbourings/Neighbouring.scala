package studies.wsi.puzzle
package neighbourings

import board.Board
import board.TupleAdd

trait Neighbouring {
  val directions: Seq[(Int, Int)] = Seq((1, 0), (-1, 0), (0, 1), (0, -1))

  def yieldSeqMove(board: Board, seqMove: Seq[(Int, Int)]): (Board, (Int, Int)) = {
    (board.move(seqMove), seqMove.fold((0, 0))((x, y) => x + y))
  }


  def getNeighbours(board: Board): Seq[(Board, (Int, Int))]
}

