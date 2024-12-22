package goals.heuristics
import goals.statistics.Statistics 

trait Heuristic {
  def getValue(statistics: Statistics): Int
}
