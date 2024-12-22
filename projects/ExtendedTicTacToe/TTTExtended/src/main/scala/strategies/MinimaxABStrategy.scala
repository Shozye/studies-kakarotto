
package strategies
import goals.Goal
import game.{Player, Game}
import StrategyUtils.*

class MinimaxABStrategy(val goal: Goal, val start_depth: Int, debug: Boolean = false, debug2: Boolean = false) extends MinimaxStrategy(debug) {
  val INVALID = -11 // (-1, -1)

  private def minimax(game: Game, last_move: Int, depth: Int, alpha: Double, beta: Double, maximizingPlayer: Boolean): Variation = {
    var new_alpha = alpha; var new_beta = beta
    val winner = game.isTerminalBest(last_move)
    if (winner != Player.NONE) { Variation(goal.calculateTerminal(winner, depth)) }
    else if (game.amountMoves == 25) { Variation(goal.evaluateDraw()) }
    else if (depth == 0) { Variation(goal.calculate(game))}
    else {
      val children = game.children() ; var i = 0

      var value = Variation(if maximizingPlayer then Int.MinValue else Int.MaxValue)
      while i < children.length do {
        val move = children(i)

        game.makeMove(move)
        val ret_minimax = minimax(game, move, depth - 1, new_alpha, new_beta, !maximizingPlayer)
        game.removeMove(move)
        if debug2 then println(ret_minimax)

        if (maximizingPlayer) {
          if ret_minimax.value > value.value then value = Variation(ret_minimax.value, ret_minimax.move.prepended(move))
          if value.value > new_beta then i=25
          else new_alpha = max(value.value, new_alpha)
        } else {
          if ret_minimax.value < value.value then value = Variation(ret_minimax.value, ret_minimax.move.prepended(move))
          if value.value < new_alpha then i=25
          else new_beta = min(new_beta, value.value)
        }
        i += 1

      }
      value

    }

  }

  override def getBestVariation(game: Game): Variation =
    minimax(game, INVALID, start_depth, Int.MinValue.toDouble, Int.MaxValue.toDouble, true)
}
