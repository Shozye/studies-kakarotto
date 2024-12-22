package studies.wsi.puzzle
package game

import board.Board

import org.scalatest.flatspec.AnyFlatSpec

class SolverUtilsTest extends AnyFlatSpec {
  behavior of "GameUtils inverts"

  it should "return 0 for a solved board" in {
    val board = Board(Vector.range(1, 16) :+ 0, (3, 3), 4)
    assert(SolverUtils.inverts(board) === 0)
  }

  it should "return the correct number of inversions for a board with one inversion" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15, 0), (3, 3), 4)
    assert(SolverUtils.inverts(board) === 1)
  }
  it should "return the correct number of inversions for a board size 5 with one inversion" in {
    val board = Board(
      Vector(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 24, 23, 0),
      (4, 4), 5
    )
    assert(SolverUtils.inverts(board) === 1)
  }

  it should "return the correct number of inversions for a board with multiple inversions" in {
    val board = Board(Vector(4, 1, 2, 3, 5, 6, 8, 7, 9, 10, 11, 14, 13, 12, 15, 0), (3, 3), 4)
    assert(SolverUtils.inverts(board) === 7)
  }

  behavior of "Board isSolvable"

  it should "return true for a solvable board of size 3" in {
    val board = Board(Vector(1,2,3,4,5,6,7,8,0), (2,2), 3)
    assert(SolverUtils.isSolvable(board))
  }

  it should "return false for an unsolvable board of size 3" in {
    val board = Board(Vector(1,2,3,4,5,6,8,7,0), (2,2), 3)
    assert(!SolverUtils.isSolvable(board))
  }

  it should "return true for a solvable board of size 4" in {
    val board = Board(Vector(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0), (3,3), 4)
    assert(SolverUtils.isSolvable(board))
  }

  it should "return false for an unsolvable board of size 4" in {
    val board = Board(Vector(1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,0), (3,3), 4)
    assert(!SolverUtils.isSolvable(board))
  }

  it should "return true for a solvable board of size 5" in {
    val board = Board(Vector(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0), (4,4), 5)
    assert(SolverUtils.isSolvable(board))
  }

  it should "return false for an unsolvable board of size 5" in {
    val board = Board(Vector(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,23,0), (4,4), 5)
    assert(!SolverUtils.isSolvable(board))
  }
}
