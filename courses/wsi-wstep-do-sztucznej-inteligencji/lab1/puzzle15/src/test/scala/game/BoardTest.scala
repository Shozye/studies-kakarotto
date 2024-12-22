package studies.wsi.puzzle
package game

import org.scalatest.flatspec.AnyFlatSpec
import studies.wsi.puzzle.board.Board

class BoardTest extends AnyFlatSpec {
  private val initBoard: Board = Board(Vector(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0), (3,3), 4)

  behavior of "Board move"

  it should "allow for horizontal move" in {
      val board = initBoard.stepMove((0,-1)).stepMove((0,-1)).stepMove((0,-1))
      assert(board.board === Vector(1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15))
      assert(board.N === 4)
      assert(board.empty === (3,0))
  }
  it should "allow for vertical move" in {
    val board = initBoard.stepMove((-1, 0)).stepMove((-1, 0)).stepMove((-1, 0))
    assert(board.board === Vector(1, 2, 3, 0, 5, 6, 7, 4, 9, 10, 11, 8, 13, 14, 15, 12))
    assert(board.N === 4)
    assert(board.empty === (0,3))
  }
  it should "allow for chaining moves" in{
    val board = initBoard.stepMove((0,- 1)).stepMove((0,-1)).stepMove((0,-1)).stepMove((-1,0)).stepMove((-1,0)).stepMove((0, 1)).stepMove((-1, 0)).stepMove((0, -1))
    assert(board.board === Vector(0, 1, 3, 4, 6, 2, 7, 8, 5, 10, 11, 12, 9, 13, 14, 15))
    assert(board.N === 4)
    assert(board.empty === (0,0))
  }
  it should "throw error when moved out of bounds"in {
    assertThrows[IndexOutOfBoundsException]{
      initBoard.stepMove((4,3))
    }
  }
  
  behavior of "Board can_move"

  it should "return true for a valid move" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 0), (2, 2), 3)
    assert(board.can_move(List((-1, 0))))
  }

  it should "return false for an invalid move outside the board" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 0), (0, 0), 3)
    assert(!board.can_move(List((-1, 0))))
  }

  it should "return false for an invalid move inside the board" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 0), (2,2), 3)
    assert(!board.can_move(List((1, 0))))
  }
}
