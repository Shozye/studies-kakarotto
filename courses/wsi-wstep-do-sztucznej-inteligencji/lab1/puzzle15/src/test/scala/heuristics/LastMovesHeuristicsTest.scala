package studies.wsi.puzzle
package heuristics
import board.Board
import org.scalatest.flatspec.AnyFlatSpec

class LastMovesHeuristicsTest extends AnyFlatSpec {
  behavior of "LastMovesHeuristics"

  it should "returns 0 for 1 move to solve" in {
    val board = Board(Vector(1, 2, 3, 4, 5, 6, 7, 0, 8), (2,2), 3)
    assert(LastMovesHeuristics.calculateFromPermutation(board, false) === 0)
  }
  it should "returns 2 for simple last move" in {
    val board = Board(Vector(8, 6, 0, 4, 5, 2, 7, 3, 1), (2,2), 3)
    assert(LastMovesHeuristics.calculateFromPermutation(board, false) === 2)
  }
  it should "return 2 for 5x5 board with 0 in goal" in {
    val board = Board(Vector(
      1, 2, 3, 4, 5,
      6, 7, 8, 9, 10,
      11, 12, 13, 14, 20,
      16, 17, 18, 19, 15 ,
      21, 22, 23, 24, 0), (4, 4), 5)
    assert(LastMovesHeuristics.calculateFromPermutation(board, false) === 2)
  }

}
