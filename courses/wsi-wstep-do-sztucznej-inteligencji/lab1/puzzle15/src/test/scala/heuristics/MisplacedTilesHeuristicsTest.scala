package studies.wsi.puzzle
package heuristics
import board.Board

import org.scalatest.flatspec.AnyFlatSpec

class MisplacedTilesHeuristicsTest extends AnyFlatSpec {
  behavior of "MisplacedTilesHeuristics"

  it should "returns correct amount for the solved board" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), (3, 3), 4)
    assert(MisplacedTilesHeuristics.calculateFromPermutation(board) === 0)
  }

  it should "returns correct amount for 2 misplaced tiles" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0), (3, 2), 4)
    assert(MisplacedTilesHeuristics.calculateFromPermutation(board) === 2)
  }

  it should "returns correct amount for board with 2 misplaced tiles" in {
    val board = Board(Vector(2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), (0, 1), 4)
    assert(MisplacedTilesHeuristics.calculateFromPermutation(board) === 2)
  }

  it should "returns correct amount for board with 4 misplaced tiles" in {
    val board = Board(Vector(1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0), (3, 2), 4)
    assert(MisplacedTilesHeuristics.calculateFromPermutation(board) === 4)
  }

  it should "returns correct amount for board with 14 misplaced tiles" in {
    val board = Board(Vector(15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0), (3, 3), 4)
    assert(MisplacedTilesHeuristics.calculateFromPermutation(board) === 14)
  }

}

