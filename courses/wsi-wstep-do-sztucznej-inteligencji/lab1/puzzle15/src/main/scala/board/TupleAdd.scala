package studies.wsi.puzzle
package board

import scala.annotation.targetName


implicit class TupleAdd(t: (Int, Int)) {
  @targetName("add")
  def +(p: (Int, Int)): (Int, Int) = (p._1 + t._1, p._2 + t._2)
  @targetName("greater")
  def >(p: (Int, Int)): Boolean = t._1 > p._1 && t._2 > p._2
  @targetName("greater_equal")
  def >=(p: (Int, Int)): Boolean = t._1 >= p._1 && t._2 >= p._2
}