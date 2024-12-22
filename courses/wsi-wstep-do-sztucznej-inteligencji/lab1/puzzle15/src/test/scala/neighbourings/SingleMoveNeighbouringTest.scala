package studies.wsi.puzzle
package neighbourings

import org.scalatest.flatspec.AnyFlatSpec
import board.Board

class SingleMoveNeighbouringTest extends AnyFlatSpec {
  behavior of "SingleMoveNeighbouring"

  it should "return all neighbours of solved board 4x4" in {
    val expected = Seq(
      (Board.from(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12)), (-1, 0)),
      (Board.from(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)), (0, -1)),
    )
    val testBoard = Board.from(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    assert(SingleMoveNeighbouring.getNeighbours(testBoard) === expected)
  }
}
