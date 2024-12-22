import bot.Bot
import strategies.{RandomLegalStrategy, TTTStrategy}

import java.net.ConnectException

object Runner {
  def runSingleBot(ip: String, port: Int, player: Int, depth: Int, strategy: TTTStrategy): Unit = {
    println(s""" Config: ip=$ip port=$port player$player depth=$depth""")
    try {
      Bot.run(ip, port, player, strategy)
    } catch {
      case _: ConnectException => println("Socket refused connection")
    }
  }
}
