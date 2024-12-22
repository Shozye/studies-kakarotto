package bot

import strategies.TTTStrategy
import game.{Game, Player}

object LocalBot {
  def run(strategy1: TTTStrategy, strategy2: TTTStrategy): Player = {
    val game = Game.Empty()

    val strategies: Array[TTTStrategy] = Array(strategy1, strategy2)
    var i = 1
    var bestMove = strategies(0).getBestMove(game)
    game.makeMoveConstant(bestMove)
    //game.printBoard()

    while {
      game.isTerminalBest(bestMove) == Player.NONE 
      && game.amountMoves < 25
    }do {
      bestMove = strategies(i).getBestMove(game)
      game.makeMoveConstant(bestMove)
      //game.printBoard()
      i = 1 - i
    }

    game.isTerminalBest(bestMove)
  }
}