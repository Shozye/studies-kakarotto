package game

import scala.collection.immutable.ArraySeq
import scala.util.Random
import scala.annotation.tailrec


class Game(var player: Player, val board: Board) {

  def makeMove(move: (Int, Int)): Unit = makeMove(move(0)*5 + move(1))
  def makeMove(move: Int): Unit = 
    amountMoves += 1
    if (amountMoves == 1) {privateChildren(1) = Game.secondMoveChildren(move)}
    board.setTile(move, player)
    swapPlayer()
  def makeMoveConstant(move: (Int, Int)): Unit = makeMoveConstant(move(0)*5 + move(1))
  def makeMoveConstant(move: Int): Unit =
    makeMove(move)
    removeChild(move)

  def removeChild(move: Int): Unit = privateChildren.mapInPlace(childGroup => childGroup.diff(List(move)))

  def swapPlayer(): Unit = player = PlayerUtils.opposite(player)

  def printBoard(): Unit = println(board)
  
  def removeMove(move: (Int, Int)): Unit = removeMove(move(0)*5 + move(1))
  def removeMove(move: Int): Unit = 
    amountMoves -= 1
    board.setTile(move, Player.NONE)
    swapPlayer()

  def get(row: Int, col: Int): Player = get(row*5 + col)
  def get(row_col: (Int, Int)): Player = get(row_col(0), row_col(1))
  def get(index: Int): Player = board.get(index)

  val CHILDREN_AMOUNT = 25
  var privateChildren  = (0 until CHILDREN_AMOUNT).map(_ => Random.shuffle(0 until 25)).toArray.updated(0, Game.firstMoveChildren)
  var amountMoves = board.board.count(player => player != Player.NONE)

  def children(): IndexedSeq[Int] = {
    privateChildren(amountMoves).filter(elem => get(elem) == Player.NONE)
  }

  def isTerminalBest(move: (Int, Int)): Player = isTerminalBest(move(0)*5 + move(1))
  def isTerminalBest(move: Int): Player = 
    if move == -11 then Player.NONE 
    else isTerminalFromLastMove(move)

  @tailrec private def winCheckAtState3(state: Array[Int], nextStates: List[Array[Int]]): Player = {
    val possible_winner = get(state(0))
    if (possible_winner != Player.NONE 
            && possible_winner == get(state(1)) && possible_winner == get(state(2)) && possible_winner == get(state(3))
    ) possible_winner 
    else if (nextStates.isEmpty) Player.NONE
    else winCheckAtState3(nextStates.head, nextStates.tail) 
  }

  @tailrec private def loseCheckAtState3(state: Array[Int], nextStates: List[Array[Int]]): Player = {
    val possible_loser = get(state(0))
    if (possible_loser != Player.NONE 
            && possible_loser == get(state(1)) && possible_loser == get(state(2))
    ) possible_loser
    else if (nextStates.isEmpty) Player.NONE 
    else  loseCheckAtState3(nextStates.head, nextStates.tail) 
  }

  private def isTerminalFromLastMove(move: Int): Player = {
    var loser = loseCheckAtState3(Game.loseStatesPerMove3(move).head, Game.loseStatesPerMove3(move).tail)
    if (loser == Player.NONE) Player.NONE
    else{
      val winner = winCheckAtState3(Game.winStatesPerMove3(move).head, Game.winStatesPerMove3(move).tail)
      if (winner != Player.NONE) then winner 
      else PlayerUtils.opposite(loser)
    } 
  }
}

object Game {
  private val firstMoveChildren: IndexedSeq[Int] = Random.shuffle(IndexedSeq(12,17,18,22,23,24))
  private val secondMoveChildren: ArraySeq[IndexedSeq[Int]] = 
    ArraySeq(
      Random.shuffle(IndexedSeq(1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 18, 19, 24)), // 0
      Random.shuffle(IndexedSeq(0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)), // 1
      Random.shuffle(IndexedSeq(0, 1, 5, 6, 7, 10, 11, 12, 15, 16, 17, 20, 21, 22)), // 2
      Random.shuffle(IndexedSeq(0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)), // 3
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 15, 16, 20)), // 4
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)), // 5
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 18, 19, 24)), // 6
      Random.shuffle(IndexedSeq(0, 1, 2, 5, 6, 10, 11, 12, 15, 16, 17, 20, 21, 22)), // 7
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 15, 16, 20)), // 8
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)), // 9
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14)), // 10
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14)), // 11
      Random.shuffle(IndexedSeq(0, 1, 2, 6, 7)), // 12
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14)), // 13
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)), // 14
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24)), // 15
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15, 20)), // 16
      Random.shuffle(IndexedSeq(0, 1, 2, 5, 6, 7, 10, 11, 12, 15, 16, 20, 21, 22)), // 17
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 19, 24)), // 18
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24)), // 19
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15, 16)), // 20
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24)), // 21
      Random.shuffle(IndexedSeq(0, 1, 2, 5, 6, 7, 10, 11, 12, 15, 16, 17, 20, 21)), // 22
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24)), // 23
      Random.shuffle(IndexedSeq(0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 18, 19)), // 24
    )


  private val winStatesPerMove: Array[Array[Array[(Int, Int)]]] = Array(
    Array(Array((0, 0), (0, 1), (0, 2), (0, 3)), Array((0, 0), (1, 0), (2, 0), (3, 0)), Array((0, 0), (1, 1), (2, 2), (3, 3))),
    Array(Array((0, 0), (0, 1), (0, 2), (0, 3)), Array((0, 1), (0, 2), (0, 3), (0, 4)), Array((0, 1), (1, 1), (2, 1), (3, 1)), Array((0, 1), (1, 2), (2, 3), (3, 4))),
    Array(Array((0, 0), (0, 1), (0, 2), (0, 3)), Array((0, 1), (0, 2), (0, 3), (0, 4)), Array((0, 2), (1, 2), (2, 2), (3, 2))),
    Array(Array((0, 0), (0, 1), (0, 2), (0, 3)), Array((0, 1), (0, 2), (0, 3), (0, 4)), Array((0, 3), (1, 3), (2, 3), (3, 3)), Array((0, 3), (1, 2), (2, 1), (3, 0))),
    Array(Array((0, 1), (0, 2), (0, 3), (0, 4)), Array((0, 4), (1, 4), (2, 4), (3, 4)), Array((0, 4), (1, 3), (2, 2), (3, 1))),
    Array(Array((1, 0), (1, 1), (1, 2), (1, 3)), Array((0, 0), (1, 0), (2, 0), (3, 0)), Array((1, 0), (2, 0), (3, 0), (4, 0)), Array((1, 0), (2, 1), (3, 2), (4, 3))),
    Array(Array((1, 0), (1, 1), (1, 2), (1, 3)), Array((1, 1), (1, 2), (1, 3), (1, 4)), Array((0, 1), (1, 1), (2, 1), (3, 1)), Array((1, 1), (2, 1), (3, 1), (4, 1)), Array((0, 0), (1, 1), (2, 2), (3, 3)), Array((1, 1), (2, 2), (3, 3), (4, 4))),
    Array(Array((1, 0), (1, 1), (1, 2), (1, 3)), Array((1, 1), (1, 2), (1, 3), (1, 4)), Array((0, 2), (1, 2), (2, 2), (3, 2)), Array((1, 2), (2, 2), (3, 2), (4, 2)), Array((0, 1), (1, 2), (2, 3), (3, 4)), Array((0, 3), (1, 2), (2, 1), (3, 0))),
    Array(Array((1, 0), (1, 1), (1, 2), (1, 3)), Array((1, 1), (1, 2), (1, 3), (1, 4)), Array((0, 3), (1, 3), (2, 3), (3, 3)), Array((1, 3), (2, 3), (3, 3), (4, 3)), Array((0, 4), (1, 3), (2, 2), (3, 1)), Array((1, 3), (2, 2), (3, 1), (4, 0))),
    Array(Array((1, 1), (1, 2), (1, 3), (1, 4)), Array((0, 4), (1, 4), (2, 4), (3, 4)), Array((1, 4), (2, 4), (3, 4), (4, 4)), Array((1, 4), (2, 3), (3, 2), (4, 1))),
    Array(Array((2, 0), (2, 1), (2, 2), (2, 3)), Array((0, 0), (1, 0), (2, 0), (3, 0)), Array((1, 0), (2, 0), (3, 0), (4, 0))),
    Array(Array((2, 0), (2, 1), (2, 2), (2, 3)), Array((2, 1), (2, 2), (2, 3), (2, 4)), Array((0, 1), (1, 1), (2, 1), (3, 1)), Array((1, 1), (2, 1), (3, 1), (4, 1)), Array((1, 0), (2, 1), (3, 2), (4, 3)), Array((0, 3), (1, 2), (2, 1), (3, 0))),
    Array(Array((2, 0), (2, 1), (2, 2), (2, 3)), Array((2, 1), (2, 2), (2, 3), (2, 4)), Array((0, 2), (1, 2), (2, 2), (3, 2)), Array((1, 2), (2, 2), (3, 2), (4, 2)), Array((0, 0), (1, 1), (2, 2), (3, 3)), Array((1, 1), (2, 2), (3, 3), (4, 4)), Array((0, 4), (1, 3), (2, 2), (3, 1)), Array((1, 3), (2, 2), (3, 1), (4, 0))),
    Array(Array((2, 0), (2, 1), (2, 2), (2, 3)), Array((2, 1), (2, 2), (2, 3), (2, 4)), Array((0, 3), (1, 3), (2, 3), (3, 3)), Array((1, 3), (2, 3), (3, 3), (4, 3)), Array((0, 1), (1, 2), (2, 3), (3, 4)), Array((1, 4), (2, 3), (3, 2), (4, 1))),
    Array(Array((2, 1), (2, 2), (2, 3), (2, 4)), Array((0, 4), (1, 4), (2, 4), (3, 4)), Array((1, 4), (2, 4), (3, 4), (4, 4))),
    Array(Array((3, 0), (3, 1), (3, 2), (3, 3)), Array((0, 0), (1, 0), (2, 0), (3, 0)), Array((1, 0), (2, 0), (3, 0), (4, 0)), Array((0, 3), (1, 2), (2, 1), (3, 0))),
    Array(Array((3, 0), (3, 1), (3, 2), (3, 3)), Array((3, 1), (3, 2), (3, 3), (3, 4)), Array((0, 1), (1, 1), (2, 1), (3, 1)), Array((1, 1), (2, 1), (3, 1), (4, 1)), Array((0, 4), (1, 3), (2, 2), (3, 1)), Array((1, 3), (2, 2), (3, 1), (4, 0))),
    Array(Array((3, 0), (3, 1), (3, 2), (3, 3)), Array((3, 1), (3, 2), (3, 3), (3, 4)), Array((0, 2), (1, 2), (2, 2), (3, 2)), Array((1, 2), (2, 2), (3, 2), (4, 2)), Array((1, 0), (2, 1), (3, 2), (4, 3)), Array((1, 4), (2, 3), (3, 2), (4, 1))),
    Array(Array((3, 0), (3, 1), (3, 2), (3, 3)), Array((3, 1), (3, 2), (3, 3), (3, 4)), Array((0, 3), (1, 3), (2, 3), (3, 3)), Array((1, 3), (2, 3), (3, 3), (4, 3)), Array((0, 0), (1, 1), (2, 2), (3, 3)), Array((1, 1), (2, 2), (3, 3), (4, 4))),
    Array(Array((3, 1), (3, 2), (3, 3), (3, 4)), Array((0, 4), (1, 4), (2, 4), (3, 4)), Array((1, 4), (2, 4), (3, 4), (4, 4)), Array((0, 1), (1, 2), (2, 3), (3, 4))),
    Array(Array((4, 0), (4, 1), (4, 2), (4, 3)), Array((1, 0), (2, 0), (3, 0), (4, 0)), Array((1, 3), (2, 2), (3, 1), (4, 0))),
    Array(Array((4, 0), (4, 1), (4, 2), (4, 3)), Array((4, 1), (4, 2), (4, 3), (4, 4)), Array((1, 1), (2, 1), (3, 1), (4, 1)), Array((1, 4), (2, 3), (3, 2), (4, 1))),
    Array(Array((4, 0), (4, 1), (4, 2), (4, 3)), Array((4, 1), (4, 2), (4, 3), (4, 4)), Array((1, 2), (2, 2), (3, 2), (4, 2))),
    Array(Array((4, 0), (4, 1), (4, 2), (4, 3)), Array((4, 1), (4, 2), (4, 3), (4, 4)), Array((1, 3), (2, 3), (3, 3), (4, 3)), Array((1, 0), (2, 1), (3, 2), (4, 3))),
    Array(Array((4, 1), (4, 2), (4, 3), (4, 4)), Array((1, 4), (2, 4), (3, 4), (4, 4)), Array((1, 1), (2, 2), (3, 3), (4, 4)))
  )

  private val winStatesPerMove3: ArraySeq[List[Array[Int]]] = ArraySeq(
    List(Array((0), (1), (2), (3)), Array((0), (5), (10), (15)), Array((0), (6), (12), (18))),
    List(Array((0), (1), (2), (3)), Array((1), (2), (3), (4)), Array((1), (6), (11), (16)), Array((1), (7), (13), (19))),
    List(Array((0), (1), (2), (3)), Array((1), (2), (3), (4)), Array((2), (7), (12), (17))),
    List(Array((0), (1), (2), (3)), Array((1), (2), (3), (4)), Array((3), (8), (13), (18)), Array((3), (7), (11), (15))),
    List(Array((1), (2), (3), (4)), Array((4), (9), (14), (19)), Array((4), (8), (12), (16))),
    List(Array((5), (6), (7), (8)), Array((0), (5), (10), (15)), Array((5), (10), (15), (20)), Array((5), (11), (17), (23))),
    List(Array((5), (6), (7), (8)), Array((6), (7), (8), (9)), Array((1), (6), (11), (16)), Array((6), (11), (16), (21)), Array((0), (6), (12), (18)), Array((6), (12), (18), (24))),
    List(Array((5), (6), (7), (8)), Array((6), (7), (8), (9)), Array((2), (7), (12), (17)), Array((7), (12), (17), (22)), Array((1), (7), (13), (19)), Array((3), (7), (11), (15))),
    List(Array((5), (6), (7), (8)), Array((6), (7), (8), (9)), Array((3), (8), (13), (18)), Array((8), (13), (18), (23)), Array((4), (8), (12), (16)), Array((8), (12), (16), (20))),
    List(Array((6), (7), (8), (9)), Array((4), (9), (14), (19)), Array((9), (14), (19), (24)), Array((9), (13), (17), (21))),
    List(Array((10), (11), (12), (13)), Array((0), (5), (10), (15)), Array((5), (10), (15), (20))),
    List(Array((10), (11), (12), (13)), Array((11), (12), (13), (14)), Array((1), (6), (11), (16)), Array((6), (11), (16), (21)), Array((5), (11), (17), (23)), Array((3), (7), (11), (15))),
    List(Array((10), (11), (12), (13)), Array((11), (12), (13), (14)), Array((2), (7), (12), (17)), Array((7), (12), (17), (22)), Array((0), (6), (12), (18)), Array((6), (12), (18), (24)), Array((4), (8), (12), (16)), Array((8), (12), (16), (20))),
    List(Array((10), (11), (12), (13)), Array((11), (12), (13), (14)), Array((3), (8), (13), (18)), Array((8), (13), (18), (23)), Array((1), (7), (13), (19)), Array((9), (13), (17), (21))),
    List(Array((11), (12), (13), (14)), Array((4), (9), (14), (19)), Array((9), (14), (19), (24))),
    List(Array((15), (16), (17), (18)), Array((0), (5), (10), (15)), Array((5), (10), (15), (20)), Array((3), (7), (11), (15))),
    List(Array((15), (16), (17), (18)), Array((16), (17), (18), (19)), Array((1), (6), (11), (16)), Array((6), (11), (16), (21)), Array((4), (8), (12), (16)), Array((8), (12), (16), (20))),
    List(Array((15), (16), (17), (18)), Array((16), (17), (18), (19)), Array((2), (7), (12), (17)), Array((7), (12), (17), (22)), Array((5), (11), (17), (23)), Array((9), (13), (17), (21))),
    List(Array((15), (16), (17), (18)), Array((16), (17), (18), (19)), Array((3), (8), (13), (18)), Array((8), (13), (18), (23)), Array((0), (6), (12), (18)), Array((6), (12), (18), (24))),
    List(Array((16), (17), (18), (19)), Array((4), (9), (14), (19)), Array((9), (14), (19), (24)), Array((1), (7), (13), (19))),
    List(Array((20), (21), (22), (23)), Array((5), (10), (15), (20)), Array((8), (12), (16), (20))),
    List(Array((20), (21), (22), (23)), Array((21), (22), (23), (24)), Array((6), (11), (16), (21)), Array((9), (13), (17), (21))),
    List(Array((20), (21), (22), (23)), Array((21), (22), (23), (24)), Array((7), (12), (17), (22))),
    List(Array((20), (21), (22), (23)), Array((21), (22), (23), (24)), Array((8), (13), (18), (23)), Array((5), (11), (17), (23))),
    List(Array((21), (22), (23), (24)), Array((9), (14), (19), (24)), Array((6), (12), (18), (24))),
  )

  private val loseStatesPerMove: Array[Array[Array[(Int, Int)]]] = Array(
    Array(Array((0, 0), (0, 1), (0, 2)), Array((0, 0), (1, 0), (2, 0)), Array((0, 0), (1, 1), (2, 2))),
    Array(Array((0, 0), (0, 1), (0, 2)), Array((0, 1), (0, 2), (0, 3)), Array((0, 1), (1, 1), (2, 1)), Array((0, 1), (1, 2), (2, 3))),
    Array(Array((0, 0), (0, 1), (0, 2)), Array((0, 1), (0, 2), (0, 3)), Array((0, 2), (0, 3), (0, 4)), Array((0, 2), (1, 2), (2, 2)), Array((0, 2), (1, 3), (2, 4)), Array((0, 2), (1, 1), (2, 0))),
    Array(Array((0, 1), (0, 2), (0, 3)), Array((0, 2), (0, 3), (0, 4)), Array((0, 3), (1, 3), (2, 3)), Array((0, 3), (1, 2), (2, 1))),
    Array(Array((0, 2), (0, 3), (0, 4)), Array((0, 4), (1, 4), (2, 4)), Array((0, 4), (1, 3), (2, 2))),
    Array(Array((1, 0), (1, 1), (1, 2)), Array((0, 0), (1, 0), (2, 0)), Array((1, 0), (2, 0), (3, 0)), Array((1, 0), (2, 1), (3, 2))),
    Array(Array((1, 0), (1, 1), (1, 2)), Array((1, 1), (1, 2), (1, 3)), Array((0, 1), (1, 1), (2, 1)), Array((1, 1), (2, 1), (3, 1)), Array((0, 0), (1, 1), (2, 2)), Array((1, 1), (2, 2), (3, 3)), Array((0, 2), (1, 1), (2, 0))),
    Array(Array((1, 0), (1, 1), (1, 2)), Array((1, 1), (1, 2), (1, 3)), Array((1, 2), (1, 3), (1, 4)), Array((0, 2), (1, 2), (2, 2)), Array((1, 2), (2, 2), (3, 2)), Array((0, 1), (1, 2), (2, 3)), Array((1, 2), (2, 3), (3, 4)), Array((0, 3), (1, 2), (2, 1)), Array((1, 2), (2, 1), (3, 0))),
    Array(Array((1, 1), (1, 2), (1, 3)), Array((1, 2), (1, 3), (1, 4)), Array((0, 3), (1, 3), (2, 3)), Array((1, 3), (2, 3), (3, 3)), Array((0, 2), (1, 3), (2, 4)), Array((0, 4), (1, 3), (2, 2)), Array((1, 3), (2, 2), (3, 1))),
    Array(Array((1, 2), (1, 3), (1, 4)), Array((0, 4), (1, 4), (2, 4)), Array((1, 4), (2, 4), (3, 4)), Array((1, 4), (2, 3), (3, 2))),
    Array(Array((2, 0), (2, 1), (2, 2)), Array((0, 0), (1, 0), (2, 0)), Array((1, 0), (2, 0), (3, 0)), Array((2, 0), (3, 0), (4, 0)), Array((2, 0), (3, 1), (4, 2)), Array((0, 2), (1, 1), (2, 0))),
    Array(Array((2, 0), (2, 1), (2, 2)), Array((2, 1), (2, 2), (2, 3)), Array((0, 1), (1, 1), (2, 1)), Array((1, 1), (2, 1), (3, 1)), Array((2, 1), (3, 1), (4, 1)), Array((1, 0), (2, 1), (3, 2)), Array((2, 1), (3, 2), (4, 3)), Array((0, 3), (1, 2), (2, 1)), Array((1, 2), (2, 1), (3, 0))),
    Array(Array((2, 0), (2, 1), (2, 2)), Array((2, 1), (2, 2), (2, 3)), Array((2, 2), (2, 3), (2, 4)), Array((0, 2), (1, 2), (2, 2)), Array((1, 2), (2, 2), (3, 2)), Array((2, 2), (3, 2), (4, 2)), Array((0, 0), (1, 1), (2, 2)), Array((1, 1), (2, 2), (3, 3)), Array((2, 2), (3, 3), (4, 4)), Array((0, 4), (1, 3), (2, 2)), Array((1, 3), (2, 2), (3, 1)), Array((2, 2), (3, 1), (4, 0))),
    Array(Array((2, 1), (2, 2), (2, 3)), Array((2, 2), (2, 3), (2, 4)), Array((0, 3), (1, 3), (2, 3)), Array((1, 3), (2, 3), (3, 3)), Array((2, 3), (3, 3), (4, 3)), Array((0, 1), (1, 2), (2, 3)), Array((1, 2), (2, 3), (3, 4)), Array((1, 4), (2, 3), (3, 2)), Array((2, 3), (3, 2), (4, 1))),
    Array(Array((2, 2), (2, 3), (2, 4)), Array((0, 4), (1, 4), (2, 4)), Array((1, 4), (2, 4), (3, 4)), Array((2, 4), (3, 4), (4, 4)), Array((0, 2), (1, 3), (2, 4)), Array((2, 4), (3, 3), (4, 2))),
    Array(Array((3, 0), (3, 1), (3, 2)), Array((1, 0), (2, 0), (3, 0)), Array((2, 0), (3, 0), (4, 0)), Array((1, 2), (2, 1), (3, 0))),
    Array(Array((3, 0), (3, 1), (3, 2)), Array((3, 1), (3, 2), (3, 3)), Array((1, 1), (2, 1), (3, 1)), Array((2, 1), (3, 1), (4, 1)), Array((2, 0), (3, 1), (4, 2)), Array((1, 3), (2, 2), (3, 1)), Array((2, 2), (3, 1), (4, 0))),
    Array(Array((3, 0), (3, 1), (3, 2)), Array((3, 1), (3, 2), (3, 3)), Array((3, 2), (3, 3), (3, 4)), Array((1, 2), (2, 2), (3, 2)), Array((2, 2), (3, 2), (4, 2)), Array((1, 0), (2, 1), (3, 2)), Array((2, 1), (3, 2), (4, 3)), Array((1, 4), (2, 3), (3, 2)), Array((2, 3), (3, 2), (4, 1))),
    Array(Array((3, 1), (3, 2), (3, 3)), Array((3, 2), (3, 3), (3, 4)), Array((1, 3), (2, 3), (3, 3)), Array((2, 3), (3, 3), (4, 3)), Array((1, 1), (2, 2), (3, 3)), Array((2, 2), (3, 3), (4, 4)), Array((2, 4), (3, 3), (4, 2))),
    Array(Array((3, 2), (3, 3), (3, 4)), Array((1, 4), (2, 4), (3, 4)), Array((2, 4), (3, 4), (4, 4)), Array((1, 2), (2, 3), (3, 4))),
    Array(Array((4, 0), (4, 1), (4, 2)), Array((2, 0), (3, 0), (4, 0)), Array((2, 2), (3, 1), (4, 0))),
    Array(Array((4, 0), (4, 1), (4, 2)), Array((4, 1), (4, 2), (4, 3)), Array((2, 1), (3, 1), (4, 1)), Array((2, 3), (3, 2), (4, 1))),
    Array(Array((4, 0), (4, 1), (4, 2)), Array((4, 1), (4, 2), (4, 3)), Array((4, 2), (4, 3), (4, 4)), Array((2, 2), (3, 2), (4, 2)), Array((2, 0), (3, 1), (4, 2)), Array((2, 4), (3, 3), (4, 2))),
    Array(Array((4, 1), (4, 2), (4, 3)), Array((4, 2), (4, 3), (4, 4)), Array((2, 3), (3, 3), (4, 3)), Array((2, 1), (3, 2), (4, 3))),
    Array(Array((4, 2), (4, 3), (4, 4)), Array((2, 4), (3, 4), (4, 4)), Array((2, 2), (3, 3), (4, 4)))
  )



  private val loseStatesPerMove3: ArraySeq[List[Array[Int]]] = ArraySeq(
    List(Array((0), (1), (2)), Array((0), (5), (10)), Array((0), (6), (12))),
    List(Array((0), (1), (2)), Array((1), (2), (3)), Array((1), (6), (11)), Array((1), (7), (13))),
    List(Array((0), (1), (2)), Array((1), (2), (3)), Array((2), (3), (4)), Array((2), (7), (12)), Array((2), (8), (14)), Array((2), (6), (10))),
    List(Array((1), (2), (3)), Array((2), (3), (4)), Array((3), (8), (13)), Array((3), (7), (11))),
    List(Array((2), (3), (4)), Array((4), (9), (14)), Array((4), (8), (12))),
    List(Array((5), (6), (7)), Array((0), (5), (10)), Array((5), (10), (15)), Array((5), (11), (17))),
    List(Array((5), (6), (7)), Array((6), (7), (8)), Array((1), (6), (11)), Array((6), (11), (16)), Array((0), (6), (12)), Array((6), (12), (18)), Array((2), (6), (10))),
    List(Array((5), (6), (7)), Array((6), (7), (8)), Array((7), (8), (9)), Array((2), (7), (12)), Array((7), (12), (17)), Array((1), (7), (13)), Array((7), (13), (19)), Array((3), (7), (11)), Array((7), (11), (15))),
    List(Array((6), (7), (8)), Array((7), (8), (9)), Array((3), (8), (13)), Array((8), (13), (18)), Array((2), (8), (14)), Array((4), (8), (12)), Array((8), (12), (16))),
    List(Array((7), (8), (9)), Array((4), (9), (14)), Array((9), (14), (19)), Array((9), (13), (17))),
    List(Array((10), (11), (12)), Array((0), (5), (10)), Array((5), (10), (15)), Array((10), (15), (20)), Array((10), (16), (22)), Array((2), (6), (10))),
    List(Array((10), (11), (12)), Array((11), (12), (13)), Array((1), (6), (11)), Array((6), (11), (16)), Array((11), (16), (21)), Array((5), (11), (17)), Array((11), (17), (23)), Array((3), (7), (11)), Array((7), (11), (15))),
    List(Array((10), (11), (12)), Array((11), (12), (13)), Array((12), (13), (14)), Array((2), (7), (12)), Array((7), (12), (17)), Array((12), (17), (22)), Array((0), (6), (12)), Array((6), (12), (18)), Array((12), (18), (24)), Array((4), (8), (12)), Array((8), (12), (16)), Array((12), (16), (20))),
    List(Array((11), (12), (13)), Array((12), (13), (14)), Array((3), (8), (13)), Array((8), (13), (18)), Array((13), (18), (23)), Array((1), (7), (13)), Array((7), (13), (19)), Array((9), (13), (17)), Array((13), (17), (21))),
    List(Array((12), (13), (14)), Array((4), (9), (14)), Array((9), (14), (19)), Array((14), (19), (24)), Array((2), (8), (14)), Array((14), (18), (22))),
    List(Array((15), (16), (17)), Array((5), (10), (15)), Array((10), (15), (20)), Array((7), (11), (15))),
    List(Array((15), (16), (17)), Array((16), (17), (18)), Array((6), (11), (16)), Array((11), (16), (21)), Array((10), (16), (22)), Array((8), (12), (16)), Array((12), (16), (20))),
    List(Array((15), (16), (17)), Array((16), (17), (18)), Array((17), (18), (19)), Array((7), (12), (17)), Array((12), (17), (22)), Array((5), (11), (17)), Array((11), (17), (23)), Array((9), (13), (17)), Array((13), (17), (21))),
    List(Array((16), (17), (18)), Array((17), (18), (19)), Array((8), (13), (18)), Array((13), (18), (23)), Array((6), (12), (18)), Array((12), (18), (24)), Array((14), (18), (22))),
    List(Array((17), (18), (19)), Array((9), (14), (19)), Array((14), (19), (24)), Array((7), (13), (19))),
    List(Array((20), (21), (22)), Array((10), (15), (20)), Array((12), (16), (20))),
    List(Array((20), (21), (22)), Array((21), (22), (23)), Array((11), (16), (21)), Array((13), (17), (21))),
    List(Array((20), (21), (22)), Array((21), (22), (23)), Array((22), (23), (24)), Array((12), (17), (22)), Array((10), (16), (22)), Array((14), (18), (22))),
    List(Array((21), (22), (23)), Array((22), (23), (24)), Array((13), (18), (23)), Array((11), (17), (23))),
    List(Array((22), (23), (24)), Array((14), (19), (24)), Array((12), (18), (24))),
  )


  val winStates: Array[Array[(Int, Int)]] =
    Array(
      Array((0, 0), (0, 1), (0, 2), (0, 3)), Array((1, 0), (1, 1), (1, 2), (1, 3)),
      Array((2, 0), (2, 1), (2, 2), (2, 3)), Array((3, 0), (3, 1), (3, 2), (3, 3)),
      Array((4, 0), (4, 1), (4, 2), (4, 3)), Array((0, 1), (0, 2), (0, 3), (0, 4)),
      Array((1, 1), (1, 2), (1, 3), (1, 4)), Array((2, 1), (2, 2), (2, 3), (2, 4)),

      Array((3, 1), (3, 2), (3, 3), (3, 4)), Array((4, 1), (4, 2), (4, 3), (4, 4)),
      Array((0, 0), (1, 0), (2, 0), (3, 0)), Array((0, 1), (1, 1), (2, 1), (3, 1)),
      Array((0, 2), (1, 2), (2, 2), (3, 2)), Array((0, 3), (1, 3), (2, 3), (3, 3)),
      Array((0, 4), (1, 4), (2, 4), (3, 4)), Array((1, 0), (2, 0), (3, 0), (4, 0)),

      Array((1, 1), (2, 1), (3, 1), (4, 1)), Array((1, 2), (2, 2), (3, 2), (4, 2)),
      Array((1, 3), (2, 3), (3, 3), (4, 3)), Array((1, 4), (2, 4), (3, 4), (4, 4)),
      Array((0, 1), (1, 2), (2, 3), (3, 4)), Array((0, 0), (1, 1), (2, 2), (3, 3)),
      Array((1, 1), (2, 2), (3, 3), (4, 4)), Array((1, 0), (2, 1), (3, 2), (4, 3)),
      
      Array((0, 3), (1, 2), (2, 1), (3, 0)), Array((0, 4), (1, 3), (2, 2), (3, 1)),
      Array((1, 3), (2, 2), (3, 1), (4, 0)), Array((1, 4), (2, 3), (3, 2), (4, 1))
    )

  val winStatesInt: Array[(Int, Int, Int, Int)] = 
    Array(
      ( 0,  1,  2,  3), 	( 5,  6,  7,  8),
      (10, 11, 12, 13), 	(15, 16, 17, 18),
      (20, 21, 22, 23), 	( 1,  2,  3,  4),
      ( 6,  7,  8,  9), 	(11, 12, 13, 14),
      (16, 17, 18, 19), 	(21, 22, 23, 24),
      ( 0,  5, 10, 15), 	( 1,  6, 11, 16),
      ( 2,  7, 12, 17), 	( 3,  8, 13, 18),
      ( 4,  9, 14, 19), 	( 5, 10, 15, 20),
      ( 6, 11, 16, 21), 	( 7, 12, 17, 22),
      ( 8, 13, 18, 23), 	( 9, 14, 19, 24),
      ( 1,  7, 13, 19), 	( 0,  6, 12, 18),
      ( 6, 12, 18, 24), 	( 5, 11, 17, 23),
      ( 3,  7, 11, 15), 	( 4,  8, 12, 16),
      ( 8, 12, 16, 20), 	( 9, 13, 17, 21),

    )
  
  val loseStatesInt: Array[(Int, Int, Int)] =
    Array(
      ( 0,  1,  2), 	( 1,  2,  3),
      ( 2,  3,  4), 	( 5,  6,  7),
      ( 6,  7,  8), 	( 7,  8,  9),
      (10, 11, 12), 	(11, 12, 13),
      (12, 13, 14), 	(15, 16, 17),
      (16, 17, 18), 	(17, 18, 19),
      (20, 21, 22), 	(21, 22, 23),
      (22, 23, 24), 	( 0,  5, 10),
      ( 5, 10, 15), 	(10, 15, 20),
      ( 1,  6, 11), 	( 6, 11, 16),
      (11, 16, 21), 	( 2,  7, 12),
      ( 7, 12, 17), 	(12, 17, 22),
      ( 3,  8, 13), 	( 8, 13, 18),
      (13, 18, 23), 	( 4,  9, 14),
      ( 9, 14, 19), 	(14, 19, 24),
      ( 2,  8, 14), 	( 1,  7, 13),
      ( 7, 13, 19), 	( 0,  6, 12),
      ( 6, 12, 18), 	(12, 18, 24),
      ( 5, 11, 17), 	(11, 17, 23),
      (10, 16, 22), 	( 2,  6, 10),
      ( 3,  7, 11), 	( 7, 11, 15),
      ( 4,  8, 12), 	( 8, 12, 16),
      (12, 16, 20), 	( 9, 13, 17),
      (13, 17, 21), 	(14, 18, 22),

    )


  val loseStates: Array[Array[(Int, Int)]] = Array(
    Array((0, 0), (0, 1), (0, 2)), Array((0, 1), (0, 2), (0, 3)), Array((0, 2), (0, 3), (0, 4)),
    Array((1, 0), (1, 1), (1, 2)), Array((1, 1), (1, 2), (1, 3)), Array((1, 2), (1, 3), (1, 4)),
    Array((2, 0), (2, 1), (2, 2)), Array((2, 1), (2, 2), (2, 3)), Array((2, 2), (2, 3), (2, 4)),
    Array((3, 0), (3, 1), (3, 2)), Array((3, 1), (3, 2), (3, 3)), Array((3, 2), (3, 3), (3, 4)),

    Array((4, 0), (4, 1), (4, 2)), Array((4, 1), (4, 2), (4, 3)), Array((4, 2), (4, 3), (4, 4)),
    Array((0, 0), (1, 0), (2, 0)), Array((1, 0), (2, 0), (3, 0)), Array((2, 0), (3, 0), (4, 0)),
    Array((0, 1), (1, 1), (2, 1)), Array((1, 1), (2, 1), (3, 1)), Array((2, 1), (3, 1), (4, 1)),
    Array((0, 2), (1, 2), (2, 2)), Array((1, 2), (2, 2), (3, 2)), Array((2, 2), (3, 2), (4, 2)),

    Array((0, 3), (1, 3), (2, 3)), Array((1, 3), (2, 3), (3, 3)), Array((2, 3), (3, 3), (4, 3)),
    Array((0, 4), (1, 4), (2, 4)), Array((1, 4), (2, 4), (3, 4)), Array((2, 4), (3, 4), (4, 4)),
    Array((0, 2), (1, 3), (2, 4)), Array((0, 1), (1, 2), (2, 3)), Array((1, 2), (2, 3), (3, 4)),
    Array((0, 0), (1, 1), (2, 2)), Array((1, 1), (2, 2), (3, 3)), Array((2, 2), (3, 3), (4, 4)),

    Array((1, 0), (2, 1), (3, 2)), Array((2, 1), (3, 2), (4, 3)), Array((2, 0), (3, 1), (4, 2)),
    Array((0, 2), (1, 1), (2, 0)), Array((0, 3), (1, 2), (2, 1)), Array((1, 2), (2, 1), (3, 0)),
    Array((0, 4), (1, 3), (2, 2)), Array((1, 3), (2, 2), (3, 1)), Array((2, 2), (3, 1), (4, 0)),
    Array((1, 4), (2, 3), (3, 2)), Array((2, 3), (3, 2), (4, 1)), Array((2, 4), (3, 3), (4, 2))
  )

  val unwinnableLoseStates: Array[Array[(Int, Int)]] = Array(
    Array((0, 2), (1, 3), (2, 4)),
    Array((2, 0), (3, 1), (4, 2)),
    Array((0, 2), (1, 1), (2, 0)),
    Array((2, 4), (3, 3), (4, 2))
  )

  def Empty(): Game = {
    Game(Player.X, Board(Array.fill(25)(Player.NONE)))
  }
}
