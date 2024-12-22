ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "3.2.2"

mainClass in assembly := Some("CommandLineMain")

lazy val root = (project in file("."))
  .settings(
    name := "TTTExtended",
  )
