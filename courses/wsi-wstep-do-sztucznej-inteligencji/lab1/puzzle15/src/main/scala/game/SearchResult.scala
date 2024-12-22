package studies.wsi.puzzle
package game


enum SearchResult:
  case Success(val distance: Int, val path: Seq[(Int, Int)], visited: Int, time: Long = -1) extends SearchResult
  case Failure extends SearchResult