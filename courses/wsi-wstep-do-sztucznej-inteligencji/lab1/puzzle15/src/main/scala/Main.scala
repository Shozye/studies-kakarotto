package studies.wsi.puzzle

import board.Board
import game.SearchResult.Failure
import game.{SearchResult, Solver, SolverUtils}
import heuristics.*
import neighbourings.SingleMoveNeighbouring

import java.io.{BufferedWriter, File, FileWriter}

object Main extends App{
  val heurs: Vector[Heuristic] = Vector(
    MisplacedTilesHeuristics,
    ManhattanDistanceHeuristics,
    ManhattanLinearConflictsHeuristics,
    ManhattanUpgraded
  )

  testHeuristicOnResources(ManhattanDistanceHeuristics, "ManhattanDistance")
  private def testHeuristicOnResources(heuristic: Heuristic, output_filename: String): Unit = {
    var data = Seq[String]()

    for {
      i <- (80 to 100)
      if (!Vector(3, 7, 12, 13, 16, 17, 18, 22, 29, 51, 62, 70, 71, 76, 91, 93, 95, 96, 99, 100).contains(i))
    } do {
      var instanceData = Seq[String]()
      val filename = s"board$i"
      val filepath = s"generated/$filename"
      val board = Board.fromResource(filepath)
      val result =
        Solver.solve(
          board,
          heuristic,
          SingleMoveNeighbouring
        )
      result match
        case SearchResult.Success(distance, path, visited, time) =>
          instanceData = instanceData :++ Seq(filename, distance.toString, visited.toString, time.toString)
        case Failure => println("XD")

      val str: String = instanceData.mkString(", ")
      println(str)

      data = data :+ str
      writeFile(
        output_filename,
        data.mkString("\n") + "\n"
      )
    }
  }

  private def createResources(amountResources: Int): Unit = {
    var i = 1
    while i <= amountResources do {
      val board = Board.getRandom(4)
      if (SolverUtils.isSolvable(board)){
        writeFile(s"src/main/resources/generated/board$i", board.board.mkString(", "))
        i+=1
      }
    }
  }

  def writeFile(filename: String, s: String): Unit = {
    val file = {
      new File(filename)
    }
    val bw = new BufferedWriter(new FileWriter(file))
    bw.write(s)
    bw.close()
  }

  private def run_tests(heuristic: Heuristic): Unit = {
    println(s"Running tests for ${heuristic.toString}")
    for (filename <- Vector(
      "simple10", "simple26",
      "easy24", "easy36",
      "medium38", "medium48",
      "hard58", "hard60"
    )) do {
      print(s"$filename: ")
      run(Board.fromResource(filename), heuristic)
    }

  }

  private def run(board: Board, heuristics: Heuristic): Unit = {
    val Result = Solver.solve(
      board,
      heuristics,
      SingleMoveNeighbouring
    )
    Result match
      case SearchResult.Success(distance, path, visited, time) =>
        report(board, distance, path, visited, time)
      case Failure => println(s"${board.board.toString()} not solvable")
  }

  private def report(board: Board, distance: Int, path: Seq[(Int, Int)], visited: Int, time: Long): Unit = {
    val timeDouble = time.toDouble
    print(s"For ${board.board.toString()} ")
    print(s"visited: $visited | ${time}ms => ${math.floor(visited/(timeDouble/1000))}/s ")
    println(s"Path: ${toDirectionString(path)} len=${path.length}")
  }

  private def toDirectionString(path: Seq[(Int, Int)]): String = {
    (for {
      move <- path
    } yield
      move match
        case (num, 0) =>
          (if (num < 0) "U" else "D")* math.abs(num)
        case (0, num) =>
          (if (num < 0) "L" else "R")* math.abs(num)
      ).mkString
  }


}
