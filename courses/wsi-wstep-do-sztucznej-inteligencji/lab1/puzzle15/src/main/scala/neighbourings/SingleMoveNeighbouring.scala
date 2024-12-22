package studies.wsi.puzzle
package neighbourings
import board.Board

object SingleMoveNeighbouring extends Neighbouring {

  override def getNeighbours(board: Board): Seq[(Board, (Int, Int))] = {
    for
      move <- directions
      seqMove = Seq(move)
      if board.can_move(seqMove)
    yield yieldSeqMove(board, seqMove)
  }
}
