
package bot

import communication.{Client, Protocol}
import game.Game
import strategies.TTTStrategy

object Bot {
  def run(ip: String, port: Int, player: Int, strategy: TTTStrategy): Unit = {
    val client = Client.fromIP(ip, port)
    Protocol.startConnection(client, player)
    val game = Game.Empty()
    var msg: String = ""
    while {
      msg = client.getMessage
      println(s"Received message $msg")
      !Protocol.isTerminateMessage(msg)
    } do {

      if !Protocol.isFirstMoveMessage(msg) then {
        // it means that it is not the first move and i need to update game
        game.makeMoveConstant(Protocol.unpackMove(msg))
        println("After enemy move")
        game.printBoard()
      }

      val move = strategy.getBestMove(game)
      game.makeMoveConstant(move)
      println("After my move")
      game.printBoard()
      Protocol.sendMove(client, move)
    }
    Protocol.handleTerminationMessage(msg)
  }
}
