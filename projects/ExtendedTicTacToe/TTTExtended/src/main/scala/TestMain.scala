
import strategies.{MinimaxABStrategy, TTTStrategy}
import game.{Game, Board}
import game.Player.*
import goals.statistics.Statistics


object TestMain {
  def test1(strategy: TTTStrategy): Unit = {
    val game = Game(
      O, 
      Board(
        Array(
          NONE, O   , NONE, NONE, NONE,
          X,    X   , NONE, NONE, NONE,
          X,    X   , NONE, O   , NONE,
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, O
        )
      )
    )
    strategy.getBestMove(game)
  }

  def test2(strategy: TTTStrategy): Unit = {
    val game = Game(
      O, 
      Board(
        Array(
          NONE, O   , NONE, NONE, NONE,
          X   , X   , NONE, NONE, NONE,
          X   , X   , NONE, O   , NONE,
          NONE, NONE, NONE, NONE, NONE,
          O   , X   , NONE, NONE, O
        )
      )
    )
    strategy.getBestMove(game)
  }
  def test3(strategy: TTTStrategy): Unit = {
    val game = Game(
      O, 
      Board(
        Array(
          NONE, O, NONE, NONE, NONE,
          X   , X, NONE, NONE, NONE,
          X   , X, NONE, O   , NONE,
          NONE, O, NONE, NONE, NONE,
          O   , X, NONE, X   , O
        )
      )
    )
    strategy.getBestMove(game)
  }

  def test4(strategy: TTTStrategy): Unit = {
    val game = Game(
      X, 
      Board(
        Array(
          NONE, O, NONE, NONE, NONE,
          X   , X, NONE, NONE, NONE,
          X   , X, NONE, O   , NONE,
          NONE, O, O   , NONE, NONE,
          O   , X, NONE, X   , O
        )
      )
    )
    strategy.getBestMove(game)
  }

  def test5(strategy: TTTStrategy): Unit = {
    val game = Game(
      O, 
      Board(
        Array(
          NONE, O, NONE, NONE, NONE,
          X   , X, NONE, X   , NONE,
          X   , X, NONE, O   , NONE,
          NONE, O, O   , NONE, NONE,
          O   , X, NONE, X   , O
        )
      )
    )
    strategy.getBestMove(game)
  }

  def test6(strategy: TTTStrategy): Unit = {
    val game = Game(
      X, 
      Board(
        Array(
          NONE, O, NONE, NONE, NONE,
          X   , X, O   , X   , NONE,
          X   , X, NONE, O   , NONE,
          NONE, O, O   , NONE, NONE,
          O   , X, NONE, X   , O
        )
      )
    )
    println(game.isTerminalBest((1,2)))
  }

  def firstMoveTest(): Unit = {
    val strategy = MinimaxABStrategy(goals.HeurMinimaxGoal2(List(1,0.1,1,0.1,1,1,1,0.1,0.1), X, 9), 9, true)
    val game = Game(
      X, 
      Board(
        Array(
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE
        )
      )
    )   
    strategy.getBestMove(game)
  }

  def winCheckHeuristicsTest(): Unit = {
    val strategy = MinimaxABStrategy(
      goals.HeurMinimaxGoal(List(), O, 1), 
      1
      )
    val game = Game(
      O, 
      Board(
        Array(
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE,
          NONE, NONE, NONE, NONE, NONE,
          X   , X   , NONE, X   , NONE
        )
      )
    )   
    assert(strategy.getBestMove(game) == (4,2), "bad")
  }

  def StatisticsFutureTableTest(): Unit = {

    val game = Game(
      O, 
      Board(
        Array(
          NONE, O   , NONE, O   , O   ,
          NONE, NONE, NONE, O   , NONE,
          NONE, NONE, NONE, NONE, O   ,
          NONE, X   , NONE, NONE, NONE,
          X   , X   , NONE, X   , NONE
        )
      )
    )   
    val statistics = Statistics.from(game)
    for {
      i <- 0 until 5
    } do {
      for {j <- 0 until 5} do {
        print(statistics.winLoseFutureTable(i*5+j))
      }
      println()
    }

  }

  def StatisticsPatternInfoTest(): Unit = {
    val game = Game(
      O, 
      Board(
        Array(
          NONE, O   , NONE, O   , O   ,
          NONE, NONE, NONE, O   , NONE,
          NONE, NONE, NONE, NONE, O   ,
          NONE, X   , NONE, NONE, X,
          X   , X   , NONE, X   , NONE
        )
      )
    )   
    val statistics = Statistics.from(game)
    println(statistics.patternInfo)

  }
  
  

  def main(args: Array[String]): Unit = {
    println("Hello World!")
    firstMoveTest()
    //StatisticsFutureTableTest()
    //winCheckHeuristicsTest()
    //StatisticsPatternInfoTest()
  }
}

