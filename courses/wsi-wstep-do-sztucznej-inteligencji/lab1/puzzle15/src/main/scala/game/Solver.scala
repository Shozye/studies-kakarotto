package studies.wsi.puzzle
package game

import board.Board
import heuristics.Heuristic
import neighbourings.Neighbouring

import java.time.Instant

object Solver {
  def solve(
             start: Board,
             heuristics: Heuristic,
             neighbouring: Neighbouring
           ): SearchResult = {
    if (!SolverUtils.isSolvable(start)){
      SearchResult.Failure
    } else {
      val before = Instant.now().toEpochMilli
      val result = Search.aStar(start, heuristics, neighbouring)
      val after = Instant.now().toEpochMilli
      SearchResult.Success(result.distance, result.path, result.visited, after-before)
    }
  }
}
