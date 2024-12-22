
package strategies

import game.{Game, Player}
import scala.util.Random

class RandomLegalStrategy() extends TTTStrategy {
  override def getBestMove(game: Game): (Int, Int) = {
    var row = Random.nextInt(5)
    var col = Random.nextInt(5)
    while (game.get(row, col) != Player.NONE){
      row = Random.nextInt(5)
      col = Random.nextInt(5)
    }
    (row, col)
  }
}
