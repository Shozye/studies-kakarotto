package game

object PlayerUtils {
  def fromInt(num: Int): Player = {
    num match
      case 1 => Player.X
      case 2 => Player.O
      case _ => Player.NONE

  }

  def opposite(player: Player): Player = {
    player match
      case Player.X => Player.O
      case Player.O => Player.X
      case Player.NONE => Player.NONE
  }
}
