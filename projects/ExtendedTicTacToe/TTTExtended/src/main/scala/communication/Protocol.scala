
package communication

object Protocol {
  def startConnection(client: Client, player: Int): Unit = {
    client.getMessage
    client.sendMessage(player.toString)
  }

  def isTerminateMessage(msg: String): Boolean = {
    msg.length == 3 && msg.charAt(0) != '6'
  }

  def handleTerminationMessage(msg: String): Unit = {

    println(
      (msg(0) match {
        case '1' => "WIN"
        case '2' => "LOSE"
        case '3' => "DRAW"
        case '4' => "WIN_ERROR"
        case '5' => "LOSE_ERROR"
      }) + " " + msg(0)
    )
  }

  def unpackMove(msg: String): (Int, Int) = {
    (msg(0).toByte-48 - 1, msg(1).toByte-48 - 1)
  }

  def isFirstMoveMessage(msg: String): Boolean = {
    msg.equals("600")
  }

  def sendMove(client: Client, move: (Int, Int)): Unit = {
    client.sendMessage(s"${move(0)+1}${move(1)+1}")
  }

}
