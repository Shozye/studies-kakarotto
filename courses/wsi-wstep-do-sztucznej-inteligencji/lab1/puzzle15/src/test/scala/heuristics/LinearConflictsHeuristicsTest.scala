package studies.wsi.puzzle
package heuristics

import board.Board
import org.scalatest.flatspec.AnyFlatSpec
class LinearConflictsHeuristicsTest extends AnyFlatSpec {
  behavior of "LinearConflictsHeuristics"

  it should "returns correct amount for the solved board 4x4" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), (3, 3), 4)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 0)
  }

  it should "returns correct amount for the solved board 3x3" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 0), (2,2), 3)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 0)
  }

  it should "return 2 for swapped 1 and 2" in {
    val board = Board(Vector(2, 1, 3, 4, 5, 6, 7, 8, 0), (2, 2), 3)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 2)
  }

  it should "return 2 for swapped 6 and 10" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 10, 7, 8, 9, 6, 11, 12, 13, 14, 15, 0), (3, 3), 4)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 2)
  }
  it should "return 4 for multiple linear conflict in one line. book example" in {
    val board = Board(Vector(1, 2, 3, 6, 5, 4, 7, 8, 0), (2, 2), 3)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 4)
  }

  it should "return 2 for not regular board. book example" in {
    val board = Board(Vector(0, 2, 1, 7,4,5,6,3,8), (2, 2), 3)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 2)
  }

  it should "return 8 for board with a lot of linear conflicts." in {
    val board = Board(Vector(7,3,2,4,6,5,1,0,8), (2,2), 3)
    assert(LinearConflictsHeuristics.calculateFromPermutation(board) === 8)
  }

}
