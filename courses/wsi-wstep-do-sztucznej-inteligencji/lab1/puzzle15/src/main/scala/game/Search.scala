package studies.wsi.puzzle
package game

import board.Board
import heuristics.Heuristic
import neighbourings.Neighbouring

import scala.collection.mutable
import game.SearchResult

import java.time.Instant

object Search {

  def reconstructPath(
                     parentTree: mutable.HashMap[Board, (Board, (Int, Int))],
                     board: Board
                     ): Seq[(Int, Int)] = {
    var totalPath = Seq[(Int, Int)]()
    var currBoard = board
    while (parentTree.contains(currBoard)) {
      val (parentBoard, path) = parentTree(currBoard)
      totalPath :+= path
      currBoard = parentBoard
    }
    totalPath.reverse
  }


  def aStar(
           start: Board,
           heuristic: Heuristic,
           neighbouring: Neighbouring
           ): SearchResult.Success = {
    val before = Instant.now().toEpochMilli
    val distances = mutable.HashMap[Board, Int]()
    val parent_tree = mutable.HashMap[Board, (Board, (Int, Int))]()
    var visited = 0
    // Initialize the start node
    distances(start) = 0

    object MinOrder extends Ordering[(Int, Int, Board)] {
      def compare(x: (Int, Int, Board), y: (Int, Int, Board)): Int = {
        val fx = x._1
        val hx = x._2
        val fy = y._1
        val hy = y._2
        val X = 1
        val Y = -1
        val DRAW = 0

        val result = if(fx < fy) {
          X
        } else if (fx == fy) {
          if (hx < hy){
            X
          } else if (hx == hy) {
            DRAW
          } else {
            Y
          }
        } else {
          Y
        }
        result
      }
    }

    val pq = mutable.PriorityQueue.empty[(Int, Int, Board)](MinOrder)
    pq.enqueue((heuristic.calculateFromPermutation(start), 0, start))

    var after = Instant.now().toEpochMilli
    // Continue searching until the priority queue is empty
    while (pq.nonEmpty) {
      val (_, _, currBoard) = pq.dequeue()
      after = Instant.now().toEpochMilli
      visited += 1
      
      // If we've found the goal, reconstruct the path and return Success
      if (currBoard.isSolved) {
        val path = reconstructPath(parent_tree, currBoard)
        return SearchResult.Success(distances(currBoard), path, visited)
      }

      // Loop through each neighbor and update the priority queue and distances
      val tentativeDistance: Int = distances.getOrElse(currBoard, Int.MaxValue-2) + 1
      for {
        (neighbor, move): (Board, (Int, Int)) <- neighbouring.getNeighbours(currBoard)
      } {

        // Update the distance if it's lower than the current distance
        if (tentativeDistance < distances.getOrElse(neighbor, Int.MaxValue)) {
          distances(neighbor) = tentativeDistance
          parent_tree(neighbor) = (currBoard, move)
          val hScore = heuristic.calculateFromPermutation(neighbor)
          val fScore = tentativeDistance + hScore
          pq.enqueue((fScore, hScore, neighbor))
        }
      }
    }

    throw Exception("Not found")
  }

}
