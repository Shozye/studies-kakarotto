
package strategies

import game.Game

trait MinimaxStrategy(debug: Boolean) extends TTTStrategy {
  def getBestVariation(game: Game): Variation

  override def getBestMove(game: Game): (Int, Int) = {
    if(game.amountMoves == 0){
      (4,3)
    } else {
      val currentTimestamp = System.currentTimeMillis()
      val best_variation = getBestVariation(game)
      val interval = System.currentTimeMillis() - currentTimestamp
      if (debug){
        println(s"Found move: ${best_variation.move.toString}, value: ${best_variation.value} in $interval")
      }
      (best_variation.move(0) / 5, best_variation.move(0) % 5)
    }
  }
}
