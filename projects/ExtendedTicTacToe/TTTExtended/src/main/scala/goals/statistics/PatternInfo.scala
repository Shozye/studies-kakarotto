package goals.statistics

class PatternInfo {
    var typeX__X4: Int = 0
    var typeXX__4: Int = 0
    var typeX___4: Int = 0
    var type_X__4: Int = 0
    var typeXX_X4: Int = 0
    var typeX_X_4: Int = 0

    var typeX__3: Int = 0
    var type_X_3: Int = 0
    var typeXX_3: Int = 0

    override def toString(): String =  {
        s"PatternInfo(X__X:$typeX__X4, XX__:$typeXX__4, X___:$typeX___4, _X__:$type_X__4, XX_X:$typeXX_X4, X_X_:$typeX_X_4" +
          s"X__:$typeX__3, _X_:$type_X_3, XX_:$typeXX_3)"
    }
}


case class BigPatternInfo (
    current: PatternInfo = PatternInfo(),
    enemy: PatternInfo = PatternInfo()
) {
    override def toString(): String = {
        s"BigPatternInfo(\n\tcurrent:$current\n\tenemy:$enemy\n)"
    }
}

