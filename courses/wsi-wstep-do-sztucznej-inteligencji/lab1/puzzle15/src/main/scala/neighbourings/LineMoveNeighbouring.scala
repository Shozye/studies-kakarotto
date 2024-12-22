package studies.wsi.puzzle
package neighbourings
import board.Board

object LineMoveNeighbouring extends Neighbouring {

  override def getNeighbours(board: Board): Seq[(Board, (Int, Int))] = {
    for {
      direction <- directions
      multipliers <- 1 until board.N
      seqMove = Seq.fill(multipliers)(direction)
      if board.can_move(seqMove)
    } yield yieldSeqMove(board, seqMove)

  }
}