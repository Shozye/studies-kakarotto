package studies.wsi.puzzle
package board
import scala.io.Source
import scala.util.Random

case object Board {
  private def toIndex(coords: (Int, Int), N: Int): Int = {
    coords(0) * N + coords(1)
  }

  private def toCoords(index: Int, N: Int): (Int, Int) = {
    (index / N, index % N)
  }

  def from(vector: Vector[Int]): Board = {
    val N = math.floor(math.sqrt(vector.length)).toInt
    Board(vector, Board.toCoords(vector.indexOf(0), N), N)
  }

  def fromResource(filename: String): Board = {
    val resource = Source.fromResource(filename)
    val vector =
      resource
        .toVector
        .mkString
        .split(", ")
        .map(x => x.strip().toInt)
        .toVector
    from(vector)
  }

  def getRandom(N: Int): Board = {
    from((Random.shuffle(1 until N*N) :+ 0).toVector)
  }

  def withMaxDistance(maxDistance: Int): Board = {
    val directions = Vector((1, 0), (-1, 0), (0, 1), (0, -1))
    var board = from(((1 until 16) :+ 0).toVector)

    var i = 0
    while (i < maxDistance) {
      val move = directions(Random.between(0, directions.length))
      if (board.can_move(Seq(move))){
        board = board.stepMove(move)
        i += 1
      }
    }
    board
  }
}

case class Board(board: Vector[Int], empty: (Int, Int), N: Int) {
  def get(row: Int, col: Int): Int = {
    board(Board.toIndex((row, col), N))
  }

  def getRow(row: Int): Vector[Int] = {
    board.slice(row * N, (row + 1) * N)
  }

  def getCol(col: Int): Vector[Int] = {
    (for row <- 0 until N yield get(row, col)).toVector
  }

  def can_move(path: Seq[(Int, Int)]): Boolean = {
    val move = path.fold((0,0))((x,y) => x+y)
    val moved = empty + move
    (N, N) > moved && moved >= (0,0)
  }

  def stepMove(move: (Int, Int)): Board = {
    val newEmpty = move + empty
    val newBoard = board.updated(Board.toIndex(empty, N), (get _).tupled(newEmpty)).updated(Board.toIndex(newEmpty, N), 0)
    Board(newBoard, newEmpty, N)
  }

  def move(seqMove: Seq[(Int, Int)]): Board = {
    var newBoard = this
    for (move <- seqMove){
      newBoard = newBoard.stepMove(move)
    }
    newBoard
  }

  def findTile(tile: Int): (Int, Int) = {
    Board.toCoords(board.indexOf(tile), N)
  }

  def isSolved: Boolean = {
    val goal = ((1 until board.length) :+ 0).toVector
    board == goal
  }
}
