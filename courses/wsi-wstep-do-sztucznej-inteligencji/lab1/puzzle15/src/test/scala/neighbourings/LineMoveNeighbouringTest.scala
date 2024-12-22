package studies.wsi.puzzle
package neighbourings

import org.scalatest.flatspec.AnyFlatSpec
import board.Board

class LineMoveNeighbouringTest extends AnyFlatSpec {
  behavior of "LineMoveNeighbouring"

  it should "return all neighbours of solved board 4x4" in {
    val expected = Seq(
      (Board.from(Vector(1,2,3,4,5,6,7,8,9,10,11,0,13,14,15,12)), (-1, 0)),
      (Board.from(Vector(1,2,3,4,5,6,7,0,9,10,11,8,13,14,15,12)), (-2, 0)),
      (Board.from(Vector(1,2,3,0,5,6,7,4,9,10,11,8,13,14,15,12)), (-3, 0)),
      (Board.from(Vector(1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,0, 15)), (0, -1)),
      (Board.from(Vector(1, 2, 3, 4,5,6,7,8,9,10,11,12,13,0,14, 15)), (0, -2)),
      (Board.from(Vector(1, 2, 3, 4,5,6,7,8,9,10,11,12,0,13,14,15)), (0, -3))
    )
    val testBoard = Board.from(Vector(1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15, 0))
    assert(LineMoveNeighbouring.getNeighbours(testBoard) === expected)
  }

  it should "return all neighbours of 4x4 board with swapped 0 and 6" in {
    val expected = Seq(
      (Board.from(Vector(1, 0, 3, 4, 5, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 6)), (-1, 0)),
      (Board.from(Vector(1, 2, 3, 4, 0, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 6)), (0, -1)),
      (Board.from(Vector(1, 2, 3, 4, 5, 7, 0, 8, 9, 10, 11, 12, 13, 14, 15, 6)), (0, 1)),
      (Board.from(Vector(1, 2, 3, 4, 5, 7, 8, 0, 9, 10, 11, 12, 13, 14, 15, 6)), (0, 2)),
      (Board.from(Vector(1, 2, 3, 4, 5, 10, 7, 8, 9, 0, 11, 12, 13, 14, 15, 6)), (1, 0)),
      (Board.from(Vector(1, 2, 3, 4, 5, 10, 7, 8, 9, 14, 11, 12, 13, 0, 15, 6)), (2, 0)),
    )
    val testBoard = Board.from(
      Vector(
        1, 2, 3, 4,
        5, 0, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 6
      )
    )
    val actual = LineMoveNeighbouring.getNeighbours(testBoard)
    expected.foreach(x => assert(actual.contains(x)))
  }
}
