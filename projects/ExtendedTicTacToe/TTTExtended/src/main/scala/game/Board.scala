
package game

class Board(val board: Array[Player]) {
  private final val SIZE = 5

  private def toIndex(row: Int, col: Int): Int = row*SIZE + col

  def get(row: Int, col: Int): Player = get(toIndex(row, col))
  def get(index: Int): Player = board(index)

  def setTile(index: Int, player: Player): Unit = board.update(index, player)
  def setTile(row: Int, col: Int, player: Player): Unit = setTile(toIndex(row, col), player)

  override def toString: String = {
    var text: String = "  "
    for i <- 1 to 5 do
      text += s"$i "
    text += "\n"
    for i <- 0 until 5 do
      text += s"${i+1} "
      for j <- 0 until 5 do
        text += s"${get(i, j).name} "
      text += "\n"
    text
  }
}
