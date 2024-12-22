package studies.wsi.puzzle
package heuristics
import board.Board

object LinearConflictsHeuristics extends Heuristic {
  def lineGenerator(board: Board): IndexedSeq[(Vector[Int], Vector[Boolean])] = {
    val iter1 = for (y <- 0 until board.N) yield {
      val row = board.getRow(y)
      (row, row.map(tile => y == getGoalY(board.N, tile)))
    }
    val iter2 = for(x <- 0 until board.N) yield {
      val col = board.getCol(x)
      (col, col.map(tile => x == getGoalX(board.N, tile)))
    }
    iter1 ++ iter2
  }

  def getLineConflicts(line: Vector[Int], goals: Vector[Boolean]): Vector[Int] = {
    val conflicts: Array[Int] = Array.fill[Int](line.length)(0)
    for {
      (pos1, (tile1, goal1)) : (Int, (Int, Boolean)) <- line.indices.zip(line.zip(goals))
    } do {
      if goal1 && !(tile1 == 0) then {
        val next_pos = pos1+1
        for {
          (pos2, (tile2, goal2)): (Int, (Int, Boolean)) <-
            (next_pos until line.length)
            .zip(
              line.slice(next_pos, line.length).zip(goals.slice(next_pos, goals.length))
            )
        } do {
          if goal2 && !(tile2 == 0) then
            if tile2 < tile1 then {
              conflicts(pos1) += 1
              conflicts(pos2) += 1
            }
        }
      }
    }
    conflicts.toVector
  }

  private def linearConflicts(board: Board): Int = {
    var dist = 0
    for (line, goals) <- lineGenerator(board) do {
      var line2 = line
      var conflicts = getLineConflicts(line2, goals)
      while conflicts.max > 0 do {
        dist += 2
        line2 = line2.updated(conflicts.zipWithIndex.maxBy(x => x._1)._2, 0)
        conflicts = getLineConflicts(line2, goals)
      }
    }
    dist

  }


  override def calculateFromPermutation(board: Board): Int = {
    linearConflicts(board)
  }

  override def calculateFromPreviousMove(board: Board, previousHeuristics: Int, previousMove: (Int, Int)): Int = {
    0
  }
}
