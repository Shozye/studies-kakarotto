package studies.wsi.puzzle
package heuristics
import board.Board
import org.scalatest.flatspec.AnyFlatSpec

class CornerTilesDistanceHeuristicsTest extends AnyFlatSpec {
  behavior of "CornerTilesDistanceHeuristics"

  it should "returns correct value for top left corner = 2" in {
    val board = Board(Vector(6, 2, 3, 4, 7, 5, 8, 9, 10, 11, 12, 13, 14, 15, 1, 0), (3, 3), 4)
    assert(CornerTilesDistanceHeuristics.calculateFromPermutation(board, false) === 2)
  }
  it should "returns correct value for top left corner = 4" in {
    val board = Board(Vector(6, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 0), (3, 3), 4)
    assert(CornerTilesDistanceHeuristics.calculateFromPermutation(board, false) === 4)
  }
  it should "returns correct value for top right corner = 2" in {
    val board = Board(Vector(1, 2, 3, 5, 4, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 0), (3, 3), 4)
    assert(CornerTilesDistanceHeuristics.calculateFromPermutation(board, false) === 2)
  }
  it should "returns correct value for top right corner = 4" in {
    val board = Board(Vector(1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), (3, 3), 4)
    assert(CornerTilesDistanceHeuristics.calculateFromPermutation(board, false) === 4)
  }
  it should "returns correct value for bottom left corner = 2" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 13, 14, 0), (3, 3), 4)
    assert(CornerTilesDistanceHeuristics.calculateFromPermutation(board, false) === 2)
  }
  it should "returns correct value for bottom left corner = 4" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 14, 13, 0), (3, 3), 4)
    assert(CornerTilesDistanceHeuristics.calculateFromPermutation(board, true) === 4)
  }
}