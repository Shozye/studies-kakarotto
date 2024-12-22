
package communication

import java.io.{BufferedReader, PrintWriter, InputStreamReader}
import java.net.Socket

class Client(
              val socket: Socket
            ) {

  val out: PrintWriter = PrintWriter(socket.getOutputStream, true)
  val in: BufferedReader = BufferedReader(InputStreamReader(socket.getInputStream))
  def getMessage: String = {
    val buffer = new Array[Char](16)
    in.read(buffer)
    val text = buffer.mkString("").trim
    println(s"""Received server message: $text""")
    text
  }
  def sendMessage(msg: String): Unit = {
    println(s"Sending message to server: $msg")
    out.println(msg)
    out.flush()
  }
}

object Client{
  def fromIP(host: String, port: Int): Client = {
    val socket = Socket(host, port)
    Client(socket)
  }
}
